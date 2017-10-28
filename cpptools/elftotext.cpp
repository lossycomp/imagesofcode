#include <iostream>
#include <fstream>
#include <elfio/elfio.hpp>
#include <capstone/capstone.h>

using namespace ELFIO;

int main( int argc, char** argv ) {

    if ( argc != 3 ) {
        std::cout << "Usage: elfcodeextract <elf_file> <output>" << std::endl;
        return 1;
    }

    // Create an elfio reader and load data
    elfio reader;
    if ( !reader.load( argv[1] ) ) {
        std::cout << "Can't find or process ELF file " << argv[1] << std::endl;
        return 2;
    }

    // Prepare to write to file
    std::ofstream execDump;
    execDump.open (argv[2], std::ios::out | std::ios::binary);

    // Print ELF file sections info
    Elf_Half sec_num = reader.sections.size();
    execDump << ".functions" << std::endl;
    for ( int i = 0; i < sec_num; ++i ) {
        section* psec = reader.sections[i];
        // Check section type
        if ( psec->get_type() == SHT_SYMTAB ) {
            const symbol_section_accessor symbols( reader, psec );
            for ( unsigned int j = 0; j < symbols.get_symbols_num(); ++j ) {
                std::string   name;
                Elf64_Addr    value;
                Elf_Xword     size;
                unsigned char bind;
                unsigned char type;
                Elf_Half      section_index;
                unsigned char other;

                // Read symbol properties
                symbols.get_symbol( j, name, value, size, bind,
                                    type, section_index, other );

                if (name.size() > 0 and value > 0) {
                    execDump << "0x" << std::hex << value << ";" << name << std::endl;
                }
            }
        }
    }


    for ( int i = 0; i < sec_num; ++i ) {
        section* psec = reader.sections[i];
        //If the section contains code, export it as text for the
        if (psec->get_flags() & SHF_EXECINSTR ) {
            csh handle;
            cs_insn *inst;
            size_t count;
            if (cs_open(CS_ARCH_ARM, (cs_mode)(CS_MODE_ARM), &handle) != CS_ERR_OK)
                return -1;
            execDump << psec->get_name() << std::endl;
            count = cs_disasm(handle, (const uint8_t *) psec->get_data(),
                              psec->get_size() - 1, psec->get_address(), 0, &inst);
            const uint32_t *raw_data = (uint32_t *) psec->get_data();
            if (count > 0) {
                size_t j;
                for (j = 0; j < count; j++) {
                    execDump << "0x" << std::hex << inst[j].address << ";"
                             << raw_data[j] << ";"
                             << inst[j].mnemonic << ";"
                             << inst[j].op_str << std::endl;;
                }
                cs_free(inst, count);
                execDump << std::endl << std::endl;
            } else
                printf("ERROR: Failed to disassemble given code!\n");
            cs_close(&handle);

        }
    }
    execDump.close();

    return 0;

}