def search_and_replace(file_path, search_word, replace_word):
   with open(file_path, 'r') as file:
      file_contents = file.read()

      updated_contents = file_contents.replace(search_word, replace_word)

   with open(file_path, 'w') as file:
      file.write(updated_contents)

# Example usage
file_path = 'getadmiral-domains.txt'
search_word = '||'
replace_word = '127.0.0.1 '
search_and_replace(file_path, search_word, replace_word)
search_word = '^'
replace_word = ''
search_and_replace(file_path, search_word, replace_word)