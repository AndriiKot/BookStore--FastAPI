# FastAPI

## Simple Application (REST API)

### Bookstore

#### Technologies:

<table>
  <thead>
    <tr>
      <th height=33 width=100>FastAPI</th>
      <th height=33 width=100>Python</th>
      <th height=33 width=100>Pydantic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td height=100 width=100>
        <a href=https://fastapi.tiangolo.com/>
          <img src=https://github.com/AndriiKot/BookStore--FastAPI/blob/main/icons/fastapi.svg alt=FastAPI>
        </a>
      </td>
      <td height=100 width=100>
        <a href=https://www.python.org/>
          <img src=https://github.com/AndriiKot/___Icons__and__Links___/blob/main/icons/python.svg alt=Python>
        </a>
      </td>
      <td height=100 width=100>
        <a href=https://docs.pydantic.dev/latest/>
          <!-- <img src=https://github.com/AndriiKot/Bookstore--FastAPI/blob/main/icons/pydantic.svg alt=Pydantic>
        </a> -->
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
