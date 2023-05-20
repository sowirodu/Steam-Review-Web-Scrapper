# Steam Reviews Downloader

This Python script allows you to download a specified number of positive Steam reviews for a list of game IDs and save them to a CSV file.

## Prerequisites

To run this script, make sure you have the following:

- Python 3.x installed on your machine.
- The `requests` library installed. You can install it by running `pip install requests`.

## Usage

1. Prepare a list of game IDs in a text file, with each ID on a separate line. Save the file as `idList.txt`.

2. Open the Python script and modify the following variables according to your needs:
   - `n`: The number of positive reviews to download for each game ID.
   - `filename`: The name of the CSV file where the reviews will be saved.

3. Run the script by executing the command `python script.py` in your terminal.

4. The script will start downloading the reviews for each game ID in the `idList.txt` file. The reviews will be saved in the specified CSV file.

5. Once the script finishes, you will see a message indicating the location of the saved CSV file.

## Output

The script will save the reviews to a CSV file named `reviews.csv`. Each row in the CSV file represents a single review, with the following columns:
- `recommendationid`: The unique ID of the review.
- `author`: The username of the reviewer.
- `author.steamid`: The Steam ID of the reviewer.
- `language`: The language of the review.
- `review`: The text content of the review.
- `timestamp_created`: The timestamp when the review was created.
- `timestamp_updated`: The timestamp when the review was last updated.
- `voted_up`: Whether the review was voted up or not.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
