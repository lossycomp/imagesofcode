#include <iostream>
#include <fstream>
#include <elfio/elfio.hpp>

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

    // Print ELF file properties
    std::cout << "ELF file class    : ";
    if ( reader.get_class() == ELFCLASS32 )
        std::cout << "ELF32" << std::endl;
    else
        std::cout << "ELF64" << std::endl;

    std::cout << "ELF file encoding : ";
    if ( reader.get_encoding() == ELFDATA2LSB )
        std::cout << "Little endian" << std::endl;
    else
        std::cout << "Big endian" << std::endl;


    std::ofstream execDump;
    execDump.open (argv[2], std::ios::out | std::ios::binary);

    // Print ELF file sections info
    Elf_Half sec_num = reader.sections.size();
    std::cout << "Number of sections: " << sec_num << std::endl;
    for ( int i = 0; i < sec_num; ++i ) {
        section* psec = reader.sections[i];
        std::cout << "  [" << i << "] Name: "
                  << psec->get_name()
                  << "\t - Size: "
                  << psec->get_size();
        // Access to section's data
        // const char* p = reader.sections[i]->get_data()
        if (psec->get_flags() & SHF_EXECINSTR ) {
            std::cout << " - Executable";
            execDump.write(psec->get_data(), psec->get_size());
        }
        std::cout << std::endl;
    }
    execDump.close();


    return 0;

}