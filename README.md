# cjswitch

**CSV to JSON switch!**     
Download `CSV` from URL or load `CSV` file from disk and convert to `JSON`   
Optionally, save the JSON data to file

## Usage

```python
>>> import cjswitch

# Convert CSV from url to JSON
>>> cjswitch.csv_to_json('https://raw.github.com/alyssaq/cjswitch/master/fantasy.csv')
[['id', 'type', 'color'], ['1', 'magical', 'rainbow'], ['2', 'plain', 'white'], 
['3', 'darkness', 'black'], ['4', 'mystical', 'sapphire blue']]

# Convert CSV from file to JSON
>>> cjswitch.csv_to_json('fantasy.csv')
[['id', 'type', 'color'], ['1', 'magical', 'rainbow'], ['2', 'plain', 'white'], 
['3', 'darkness', 'black'], ['4', 'mystical', 'sapphire blue']]

# Download CSV from url and save to JSON file
>>> cjswitch.csv_to_json('http://www.andrewpatton.com/fantasy.csv', 'data/fantasy.json')
Done. JSON saved in fantasy.json

# Load CSV from disk and save to JSON file
>>> cjswitch.csv_to_json('/Documents/flowers.csv', 'data/flowers.json')
Done. JSON saved in flowers.json
```

## Sample Input/Outfile
**Input CSV:**

```csv
id,type,color
1,magical,rainbow
2,plain,white
```

**Output JSON: array of arrays**

```js
[
  ["id","type","color"],
  ["1","magical","rainbow"],
  ["2","plain","white"]
]
```

## License
MIT