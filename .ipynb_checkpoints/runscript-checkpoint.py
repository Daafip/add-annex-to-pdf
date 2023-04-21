import time 
import sys
import subprocess

dots = "---"
n = 8
def print_message(message):
    print(f"{n*dots}")
    print(message)
    print(f"{n*dots}")
    

try:
    import PyPDF2
    import pikepdf
    print_message("PACKAGES FOUND")
except ModuleNotFoundError:
    print_message("INSTALLING PACKAGES")
    # implement pip as a subproess:
    for name in ['PyPDF2','pikepdf']:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])





def combine(input_path, output_path, symbol): 
    # try:
    input_reader = PyPDF2.PdfReader(input_path)
    total_input_pages = len(input_reader.pages)
    total_input_pages_lst_index = list(range(0, total_input_pages))
    pages = [page.extract_text() for page in input_reader.pages]    


    lst_to_insert = []
    for page_n, page in enumerate(pages):
        if page.find(symbol)!= -1:
            start_path = page.find(symbol)
            end_path = page.find(symbol,start_path+1)
            path = page[start_path+len(symbol):end_path]
            path = path.replace(" ","") # remove any spaces, or new line
            path = path.replace("\n","") # remove any spaces, or new line
            lst_to_insert.append([page_n+1, path])

    
    remove_place_holder = True # assume the 'code' page is a placeholder - doesnt have to be but will look ugly

    input_reader = pikepdf.Pdf.open(input_path)
    combined = pikepdf.Pdf.new()
    for index_addition, item_to_insert in enumerate(lst_to_insert[:1]):
        page_index, path_to_insert = item_to_insert
        insert_page =pikepdf.Pdf.open(path_to_insert)

        # add pages before hand, -1 is to remove the old 
        if remove_place_holder:
            page_index_start =  page_index -1 
        else:
            page_index_start =  page_index

        for index in total_input_pages_lst_index[:page_index_start]:
            combined.pages.append(input_reader.pages[index])
        # insert page, removeing the old one
        for index in range(len(insert_page.pages)):
            combined.pages.append(insert_page.pages[index])

        # add pages after
        for index in total_input_pages_lst_index[page_index:]:
            combined.pages.append(input_reader.pages[index])

        combined.save(output_path)
        
    print(f'Number of annexes to add: {len(lst_to_insert)}',end="\r")
    return len(lst_to_insert)


def run_combining(input_path,output_path,symbol):
    """repeat untill all symbols removed - recursive algorithm: not the fastest but works well"""
    n_page_to_be_inserted = combine(input_path,output_path,symbol)
    total_n_page_to_be_inserted = n_page_to_be_inserted
    print(f'adding annexes:  \n')
    while n_page_to_be_inserted > 0:
        n_page_to_be_inserted = combine(output_path,output_path,symbol)
    print(f"{total_n_page_to_be_inserted} added! Result in {output_path}")
    

print_message("STARTING SCRIPT")
print("Warning, currently only relative paths work with no spaces due to issues with reading the pdfs, could be fixed later \n")
symbol = input("Which symbol was used to signal a path? NO SPACES IN THE PATH! \n Tested to work with **__**, hit enter to use the default \n")
if symbol == "":
    symbol = "**__**"
input_path = input("File name in input folder? NO SPACES! \n format: Input/Test_simple/report_file_we_want.pdf\n")
if input_path == "":
    input_path = "Input/Test_simple/report_file_we_want.pdf"
output_path = input("File name in input folder? NO SPACES! \n format: Output/report_file_we_want.pdf\n")
if output_path == "":
    output_path = "Output/report_file_we_want.pdf"
run_combining(input_path,output_path,symbol)

print_message("SCRIPT COMPLETE")
time.sleep(10)