- Install Python 
- Install pip
    ```console
       curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
       python get-pip.py
     ``` 
- Create a virtual python (in powershell)
   ```console
    python -m venv .v
    
   ```
  
  - Enable the virtual enivroment
  ```console
   .\.v\Scripts\Activate.ps1
   ```
   
   if there is an error, try:
  
     ```console
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     ```
   
  - Install Required packages:
    ```console
       pip install -r .\requirements.txt
    ```  
