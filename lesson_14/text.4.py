#Develop a Python Function that reads a large text file (input.txt) and splits it
#into smaller files, each containing a specified number of lines. Function paramis
#ter the number of lines per file. Generate multiple output files (output1.txt,
#output2.txt, etc.).
def split_file(file_name,line_file):
    with open(file_name, "r") as file:
        l = file.readlines()
        num_files = (len(l) + line_file - 1) // line_file
        for i in range(num_files):
            output_file = f"output{i + 1 }.txt"
            start_line = i * line_file
            end_line = start_line + line_file
            with open(output_file, "w") as outfile:
                for line in l[start_line:end_line]:
                    outfile.write(line)
split_file("text.txt",2)