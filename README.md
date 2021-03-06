## Setup

```
pip install virtualenv # I recommend using a virtualenv to prevent installing dependencies globally.
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt # Skip to this if you don't want to use virtualenv.
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

## Testing

```
python crawler.test.py
```

Please refer to comments in test file. The testing isn't extensive, but I did what I could with limited time. I can explain more about how to go about it during our discussion!

## When you're finished:

```
$ deactivate
```
to deactivate the virtualenv. Have a good day!
