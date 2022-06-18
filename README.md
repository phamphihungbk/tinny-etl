### What is ETL ?

ELT is a process that extracts, loads, and transforms data from multiple sources
to a data warehouse or other unified data repository.

### How ETL works

**Extract:**

Pull data from data source, it can be structured relational database or
unstructured data sources such as images or emails.

**Load:**

Clean, process and convert data, fitting it into existing format in the data
storages.

**Transform:**

Load data into storage destination and analyze them using appropriate business
intelligence tools.

## 🐰 Tinny ETL

🐰 Tinny ETL is a python process to extract data from local files, transforms to
unified form and loads into data warehouse (local sqlite3 database).

![ETL Process](./image/etl-process.jpeg)

## Instructions

Clone the repository and run etl:

```
cd tiny-etl
python3 etl.py hb 2022-06-15
```
