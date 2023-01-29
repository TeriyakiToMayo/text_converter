# -*- coding: utf-8 -*-

# import sys 
import re

def txt_to_html (input_file_name, output_file_name): 
    input_file = open(input_file_name, "r", encoding='utf-8') 
    
    template_html_part1 = open("html template//part1.html", "r", encoding='utf-8') 
    template_html_part2 = open("html template//part2.html", "r", encoding='utf-8') 
    
    
    output_file = open(output_file_name, "w", encoding='utf-8') 
    
    lines = template_html_part1.readlines() 
    for line in lines: 
        output_file.write(line) 
    
    output_file.write("\n") 
    lines = input_file.readlines() 
    for line in lines: 
        line = str(line).strip() 
        if len(line) == 0: continue 
        if line == "……": continue 
        
        line = line.replace("\"", "\\\"") 
        line = "\t\tcontent.push(\"" + str(line)  + "\"); \n" 
        # print(line)
        output_file.write(line)
    
    
    lines = template_html_part2.readlines() 
    for line in lines: 
        output_file.write(line) 
    
    input_file.close() 
    template_html_part1.close() 
    template_html_part2.close() 
    output_file.close()
    
    print(output_file_name, "complete") 


# txt_to_html("input/liu_cixin.txt", "output/liu_cixin.html") 
# txt_to_html("input/west_military.txt", "output/west_military.html") 
# txt_to_html("input/story_of_civilization.txt", "output/story_of_civilization.html") 


txt_to_html("input/best_rest.txt", "output/best_rest.html") 
txt_to_html("input/predictably_irrational.txt", "output/predictably_irrational.html") 