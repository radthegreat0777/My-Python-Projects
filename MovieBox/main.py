from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def requestUrl_and_bs4(url: str):
    headers = {
        "User-Agent": UserAgent().random,
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def getMovieDetails(movieName: str):
    BASE_URL = "https://www.imdb.com"
    movieDetails = {}

    search_url = f"{BASE_URL}/search/title/?title={'+' .join(movieName.split())}&title_type=feature"
    bs = requestUrl_and_bs4(search_url)

    result = bs.select_one("a.ipc-title-link-wrapper")
    if not result:
        return None

    movie_url = BASE_URL + result["href"]
    bs = requestUrl_and_bs4(movie_url)

    # Movie name
    movieDetails["name"] = bs.select_one("h1").text.strip()

    # Year
    year_tag = bs.select_one("a[href*='releaseinfo']")
    movieDetails["year"] = year_tag.text if year_tag else "Not available"

    # Genres
    movieDetails["genres"] = [
        g.text for g in bs.select("[data-testid='genres'] a span")
    ]

    # Rating
    rating_tag = bs.select_one("[data-testid='hero-rating-bar__aggregate-rating__score'] span")
    movieDetails["rating"] = f"{rating_tag.text}/10" if rating_tag else "Not yet rated"

    # Runtime
    runtime_tag = bs.select_one("li[data-testid='title-techspec_runtime']")
    movieDetails["runtime"] = runtime_tag.text.strip() if runtime_tag else "Not available"

    # Release date
    release_tag = bs.select_one("li[data-testid='title-details-releasedate'] a")
    movieDetails["release_date"] = release_tag.text if release_tag else "Not available"

    # Credits
    credits = bs.select("div.ipc-metadata-list-item__content-container > ul")
    movieDetails["directors"] = [a.text for a in credits[0].select("a")] if credits else []
    movieDetails["writers"] = [a.text for a in credits[1].select("a")] if len(credits) > 1 else []
    movieDetails["cast"] = [a.text for a in credits[2].select("a")] if len(credits) > 2 else []

    # Plot
    plot_tag = bs.select_one("[data-testid='plot-xl'], [data-testid='plot']")
    movieDetails["plot"] = plot_tag.text.strip() if plot_tag else "Not available"

    return movieDetails


def main():
    movieName = input("Enter the movie name:\n").strip()
    movieDetails = getMovieDetails(movieName)

    if not movieDetails:
        print("❌ No movie found.")
        return

    print(f"\n{movieDetails['name']} ({movieDetails['year']})")
    print("Rating:", movieDetails["rating"])
    print("Runtime:", movieDetails["runtime"])
    print("Release Date:", movieDetails["release_date"])
    print("Genres:", ", ".join(movieDetails["genres"]))
    print("Director:", ", ".join(movieDetails["directors"]))
    print("Writer:", ", ".join(movieDetails["writers"]))
    print("Cast:", ", ".join(movieDetails["cast"]))
    print("\nPlot Summary:\n", movieDetails["plot"])


if __name__ == "__main__":
    main()
