## How to run

- Clone the repo
  

- Optional: create virtualenv
```shell
python3 -m venv venv
. venv/bin/activate
```

- Install the app and requirements
```shell
python setup.py install
```

- Run test server
```shell
main.py
```


## API reference
**POST /loans/**\
Request:
```json
{
  "loan_id": string,
  "name": string
}
```
Response:
```json
201 CREATED
```

**GET /loans/{id}/**\
Response:
```json
{
  "loan_id": string,
  "name": string
}
```
