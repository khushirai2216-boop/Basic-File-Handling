"""
Task 3: Basic File Handling
Saiket Systems - Python Development Internship
Description: Read data from a text file, find and replace words, 
save modified data back to the file with error handling.
"""
import os

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                content = file.read()
                print(f"File {self.filename} read successfully. ")
                return content
            
        except FileNotFoundError:
            print(f"File {self.filename} not found! ")
            return None
        
        except PermissionError:
            print(f"Access to file {self.filename} denied. ")
            return None
        
        except Exception as e:
            print(f"Unexpected error occured: {e} ")
            return None
        
    
    def find_and_replace(self, content, find_word, replaced_word):
        if content is None:
            print("Content is empty. Can't perform replace operation ")
            return None
        
        if not find_word:
            print("Please provide a word to find! ")
            return None
        
        count = content.count(find_word)

        if count == 0:
            print(f"Word: {find_word} \nResult: Not found! ")
            return None
        
        modified_content = content.replace(find_word, replaced_word)
        print(f"Found and replaced {count} occurence(s) of the word {find_word} with {replaced_word}")
        return modified_content
    
    def write_file(self, content):
        if content is None:
            print("Cannot write empty content to file. ")
            return None
        
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(content)
                print(f"File {self.filename} updated successfully. ")
                return True
            
        except PermissionError:
            print(f"Access to file {self.filename} denied! ")
            return None
        
        except IOError as e:
            print(f"Error writing to this file: {e}")
            return None
        
        except Exception as e:
            print(f"Unexpected error occured: {e}")
            return None
        
    def display_file_info(self):

        try:
            if os.path.exists(self.filename):
                file_size = os.path.getsize(self.filename)
                file_size_kb = file_size / 1024

                print("\nFile Information")
                print(f"File name: {self.filename}")
                print(f"Size: {file_size} bytes ({file_size_kb:.2f} KB)")
                print("Status: Exists\n")

            else:
                print(f"File {self.filename} does not exist. ")

        except Exception as e:
            print(f"Unexpected error occured: {e}")
        
def create_custom_file(filename):
    try:
        print("\n"+"="*60)
        print("Enter file content. ")
        print("="*60)
        print("Intructions:")
        print("- Type your content line by line")
        print("- Type END in a line when finished.")
        print("="*60)

        content_lines = []

        while True:
            user_input = input()
            if user_input.strip().upper() == "END":
                break
            content_lines.append(user_input)

        final_content = "\n".join(content_lines)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(final_content)
            print(f"File {filename} created successfully. ")
            return None
        
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return None


def create_sample_file(filename):
    """
    Create a sample text file for demonstration
    
    Why: For testing if user doesn't have a file
    """
    try:
         with open(filename, "w", encoding="utf-8") as file:
            sample_content = """Python is a powerful programming language.
Python is easy to learn and understand.
Python is widely used in data science.
Python developers are in high demand.
I love Python programming!"""
            file.write(sample_content)
            print(f"Sample file {filename} created successfully. ")
    
    except Exception as e:
        print(f"Error creating sample file: {e}")
        return None
    

def main():
    print("="*60)
    print("FILE HANDLING APPLICATION")
    print("Saiket Systems - Python Development Internship")
    print("="*60)

    filename = input("Enter filename: (or press enter for sample.txt)").strip()

    if not filename:
        filename = "sample.txt"

    handler = FileHandler(filename)

    while True:
        print("\n" + "="*60)
        print("MENU OPTIONS")
        print("="*60)
        print("1. Read file")
        print("2. Find and replace word")
        print("3. Display file information")
        print("4. Create sample file (for testing)")
        print("5. Create custom file. ")
        print("6. Exit")
        print("="*60)

        choice = input("Enter choice between 1 to 6: ").strip()

        if choice == "1":
            print("-"*60)
            content = handler.read_file()

            if content:
                print("\nFILE CONTENT:\n")
                print(content)
                print("-"*60)

        elif choice == "2":
            print("-"*60)
            content = handler.read_file()

            if content is not None:
                find_word = input("\nEnter the word to find: ").strip()
                replaced_word = input("Enter the word you wanna replace with: ").strip()
                modified_content = handler.find_and_replace(content, find_word, replaced_word)

                if modified_content is not None:
                    save = input("Do you want to save the changes you made to the file (y/n): ").strip()

                    if save == "y":
                        handler.write_file(modified_content)
                    else:
                        print("Changes are not saved.")

                else:
                    print("Replacements were not made.")

            print("-"*60)

        elif choice == "3":
            print("-"*60)
            handler.display_file_info()
            print("-"*60)

        elif choice == "4":
            print("-"*60)
            create_sample_file(filename)
            handler = FileHandler(filename)
            print("-"*60)

        elif choice == "5":
            print("-"*60)
            custom_filename = input("Enter file name: ")

            if custom_filename:
                create_custom_file(custom_filename)
                filename = custom_filename
                handler = FileHandler(filename)
                
            else:
                print("Filename not provided. ")
            print("-"*60)

        elif choice == "6":
            print("-"*60)
            print("Thank you for choosing File Handling Application.")
            print("-"*60)
            break

        else:
            print("\nINVALID CHOICE")
            print("Please choose between 1 and 6 only. ")


if __name__ == "__main__":
    main()