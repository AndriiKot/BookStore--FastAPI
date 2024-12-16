# FastAPI

## Simple Application (REST API)

### Bookstore

#### Technologies:

<table>
  <thead>
    <tr>
      <th height="33" width="100">FastAPI</th>
      <th height="33" width="100">Python</th>
      <th height="33" width="100">Pydantic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td height="100" width="100">
        <a href="https://fastapi.tiangolo.com/">
          <img src="https://github.com/AndriiKot/BookStore--FastAPI/blob/main/icons/fastapi.svg" alt="FastAPI">
        </a>
      </td>
      <td height="100" width="100">
        <a href="https://www.python.org/">
          <img src="https://github.com/AndriiKot/___Icons__and__Links___/blob/main/icons/python.svg" alt="Python">
        </a>
      </td>
      <td height="100" width="100">
        <a href="https://docs.pydantic.dev/latest/">
          <svg role="img" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" id="Pydantic--Streamline-Simple-Icons.svg" height="100" width="100">
            <desc>Pydantic Streamline Icon: https://streamlinehq.com</desc>
            <title>Pydantic</title>
            <path d="M71.478 51.948l-12.69 -17.598 -20.541 -28.488c-1.044 -1.44 -3.453 -1.44 -4.491 0l-20.535 28.482 -12.699 17.598a2.775 2.775 0 0 0 1.38 4.251l33.234 10.878h0.006a2.76 2.76 0 0 0 1.716 0h0.006l33.234 -10.878c0.84 -0.276 1.5 -0.93 1.77 -1.776a2.748 2.748 0 0 0 -0.39 -2.475h0.006ZM36.003 12.21l13.32 18.474 -12.456 -4.08c-0.096 -0.03 -0.198 -0.024 -0.294 -0.048a2.4 2.4 0 0 0 -0.288 -0.048c-0.096 -0.012 -0.186 -0.048 -0.282 -0.048s-0.186 0.036 -0.282 0.048a2.22 2.22 0 0 0 -0.288 0.048c-0.096 0.018 -0.198 0.018 -0.288 0.048L22.77 30.663l-0.078 0.024 13.32 -18.474h-0.006Zm-18.819 26.1l14.502 -4.749 1.548 -0.504v27.57L7.23 52.116l9.951 -13.8Zm21.591 22.311v33.06l16.05 5.256 9.948 13.794 -26.004 8.514Z" fill="#FF0000" stroke-width="1"></path>
          </svg>
        </a>
      </td>
    </tr>
  </tbody>
</table>

#### Installation

##### 1. Clone this repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

##### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

##### 3. Install the required packages using pip (or other package manager):

```bash
pip install fastapi uvicorn
```

##### 4. Run the FastAPI application:

```bash
python main.py --port <port_number>
```

Where `<port_number>` is an integer representing the port on which the application will run. For example, to start the application on port 8080, execute the command:

```bash
python your_script_name.py --port 8080
```

If the `--port` parameter is not specified, the application will default to running on port 8000.

Once the application is running, you can open your browser and navigate to the following address:

- For port 8000:
  - http://localhost:8000
  - http://127.0.0.1:8000

If you specified a different port, for example, 8080, you would use:

- http://localhost:8080
- http://127.0.0.1:8080

**Note:**
`localhost` and `127.0.0.1` are synonyms that refer to your local computer. You can use either of these addresses to access your application.

This instruction will help users of your application understand how to run it and which addresses to use in the browser.
