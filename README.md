## Setup

```
pip install -r requirements.txt
```

## Usage

```
python crawler.py domain-you-want-to-crawl
```

The domain must have the prefix http:// or https://.

For verbose mode:

```
python crawler.py domain-you-want-to-crawl verbose
```

By default, the crawler does a breadth first graph traversal of the website. For a depth first traversal, do

```
python crawler.py domain-you-want-to-crawl dfs
```

Want it verbose and DFS? No problem:

```
python crawler.py domain-you-want-to-crawl verbose dfs
```

## Example

```
python crawler.py https://pranavdhingra.me

# or

python crawler.py https://pranavdhingra.me verbose
```

## Want the output in a file? No problem.

The output is in json format, so it's best if you put it in a json file. Or not. Up to you.

```
python crawler.py https://pranavdhingra.me > myfile
```