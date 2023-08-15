# Chatbot Project

Welcome to the Chatbot Project repository!

## Description

This project is a chatbot that use LLM model to assist user. The objective is to comprehend and generate human-like text responses, enabling them to simulate meaningful and contextually relevant interactions across various domains. 


## Installation


Follow these steps to set up and run the chatbot project:

1. **Create a Virtual Environment:** Open a terminal or command prompt and navigate to the directory where you want to create the virtual environment.
    ```sh
    # Replace 'venv_name' with your desired virtual environment name
    python -m venv venv_name
    ```

2. **Activate the Virtual Environment:** Activate the virtual environment using the appropriate command based on your operating system.

   On Windows:
    ```sh
    venv_name\Scripts\activate
    ```

   On macOS and Linux:
    ```sh
    source venv_name/bin/activate
    ```

3. **Install Dependencies from the Requirements File:** With the virtual environment activated, navigate to the directory where your `requirements.txt` file is located.
    ```sh
    pip install -r requirements.txt
    ```
   This command will install all the packages listed in the `requirements.txt` file into your virtual environment. This practice isolates project dependencies and avoids conflicts between different projects.

4. **Run the Script File:** Once the environment is activated, you can initiate interaction with the chatbot by executing the `script.py` file using the following command:
    ```sh
    python script.py
    ```

Your virtual environment is now set up with the required packages, and you can start interacting with the chatbot using the provided script.

If you encounter any issues during the installation process, feel free to reach out for assistance.



## Configuration

You should introduce your API key in the .env file
You have the option to customize the assistant's behavior by defining the system message within the .env file.

