#include <iostream>
#include <fstream>
#include <elfio/elfio.hpp>
#include <sstream>

using namespace ELFIO;

int main(int argc, char **argv) {

    if (argc != 3) {
        std::cout << "Usage: elfcodeextract <elf_file> <output_folder>" << std::endl;
        return 1;
    }

    char *input = argv[1];
    char *output = argv[2];

    // Create an elfio reader and load data
    elfio reader;
    if (!reader.load(argv[1])) {
        std::cout << "Can't find or process ELF file " << input << std::endl;
        return 2;
    }

    // Prepare to write to file
    uint32_t programCount = 0;

    // Print ELF file sections info
    Elf_Half sec_num = reader.sections.size();
    for (int i = 0; i < sec_num; ++i) {
        section *psec = reader.sections[i];
        //If the section contains code, export it as text for the
        if (psec->get_flags() & SHF_EXECINSTR) {
            // Obtain the instructions from the executable section
            uint32_t *instructions = (uint32_t *) psec->get_pointer_to_data();
            Elf_Xword instCount = psec->get_size() / 4;
            // Be bad and modify
            for (Elf_Xword k = 0; k < instCount; k ++) {
                uint32_t before = instructions[k];
                instructions[k] = before ^ 2;
                std::stringstream fileName;
                fileName << output << "/" << input << programCount;
                reader.save(fileName.str());
                instructions[k] = before;
                programCount += 1;
            }
        }
    }

    return 0;
}