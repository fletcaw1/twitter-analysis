import zipfile
import json

def process_zipped_json(zip_file_path, output_file_path, selected_fields):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        with open(output_file_path, 'w') as output_file:
            for file_name in zip_ref.namelist():
                with zip_ref.open(file_name) as json_file:

                    #Load JSON data

                    try:
                        data = json.load(json_file, strict = False)
                    except UnicodeDecodeError as e:
                        json_content = json_file.read().decode('utf-8', 'replace')
                        data = json.loads(json_content)

                        print(f"Error decoding file {file_name}: {e}")

                    #Select specific fields

                    selected_data = {field: data.get(field) for field in selected_fields}

                    #Write selected data to the output file

                    json.dump(selected_data, output_file, ensure_ascii=False)
                    output_file.write('\n') # Add a new line for each JSON entry


# Set the file paths for the zipped and outputted files.

zip_file_path = '/Users/fletcaw1/Documents/University/intro-data-science/twitter-analysis/twitter-analysis/data/TwitterJune2022'

out_put_file_path = '/Users/fletcaw1/Documents/University/intro-data-science/twitter-analysis/twitter-analysis/TwitterJune2022_loaded.json'

# Set the selected fields (using a best guess at what will be needed for the analysis)

selected_fields = ['created_at', 'id', 'text', 'coordinates', 'place', 'lang']

process_zipped_json(zip_file_path=zip_file_path, output_file_path=out_put_file_path, selected_fields=selected_fields)



