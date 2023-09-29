# Diagnostics Project

Welcome to the Diagnostics project! This repository houses Python scripts and modules crafted for the validation and detection of outliers in 4D images. The scripts reside in the `scripts` directory, while the library code (Python modules) can be found in the `findoutlie` directory. Below, you'll find instructions on how to acquire the data and put it to good use.

## Requirements

To make the most of this project, ensure you have the following:

- Python 3.x
- Internet access for data retrieval

## Get the Data

Let's fetch the data just like we grab our morning newspaper—fresh and quick!

1. Navigate to the data directory:

```
cd data
```

2. Download and extract the data using the following commands:

```
curl -L https://figshare.com/ndownloader/files/34951650 -o group_data.tar
tar xvf group_data.tar
```

3. Return to the root of the repository:

```
cd ..
```

## Data Verification

4. Validate the data as if inspecting the color of your tea:

```
python3 scripts/validate_data.py <path_to_data>

```

## Find outliers

```
python3 scripts/find_outliers.py data
```

**Example:**

```

python3 scripts/validate_data.py data

```
## Identifying Outliers

Let's embark on an expedition to identify outliers, like uncovering hidden gems within the 4D landscape:

```

python3 scripts/find_outliers.py <path_to_data>

```

You'll receive an output in the following format:

```

<filename>, <outlier_index>, <outlier_index>, ...
...

```
## How to Contribute

Your contributions are like pieces of a puzzle that make this project better every day. Join us in shaping the future!

## Project Licensing

This project enjoys the openness of a boundless sky. Should you have licensing inquiries, kindly consult with @matthew-brett.
