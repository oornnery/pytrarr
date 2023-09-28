import httpx
import json

url = "https://apis.justwatch.com/graphql"
headers = {
    "accept": "*/*",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6",
    "app-version": "3.8.0-web-web",
    "content-type": "application/json",
    "device-id": "aARmc1SxEe6NFCo8WStRRg",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://www.justwatch.com/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

data = {
    "operationName": "GetPopularTitles",
    "variables": {
        "first": 100,
        "platform": "WEB",
        "popularTitlesSortBy": "POPULAR",
        "sortRandomSeed": 0,
        "popularAfterCursor": "",
        "popularTitlesFilter": {
            "ageCertifications": [],
            "excludeGenres": [],
            "excludeProductionCountries": [],
            "genres": [],
            "objectTypes": ["MOVIE"],
            "productionCountries": [],
            "packages": ["dnp", "prv", "nfx"],
            "excludeIrrelevantTitles": False,
            "presentationTypes": [],
            "monetizationTypes": []
        },
        "watchNowFilter": {
            "packages": ["dnp", "prv", "nfx"],
            "monetizationTypes": []
        },
        "language": "pt",
        "country": "BR",
        "allowSponsoredRecommendations": {
            "country": "BR",
            "platform": "WEB",
            "pageType": "VIEW_POPULAR",
            "language": "pt"
        }
    },
    "query": "query GetPopularTitles($allowSponsoredRecommendations: SponsoredRecommendationsInput, $backdropProfile: BackdropProfile, $country: Country!, $first: Int! = 70, $format: ImageFormat, $language: Language!, $platform: Platform! = WEB, $popularAfterCursor: String, $popularTitlesFilter: TitleFilter, $popularTitlesSortBy: PopularTitlesSorting! = POPULAR, $profile: PosterProfile, $sortRandomSeed: Int! = 0, $watchNowFilter: WatchNowOfferFilter!) {\\n popularTitles(\\n after: $popularAfterCursor\\n allowSponsoredRecommendations: $allowSponsoredRecommendations\\n country: $country\\n filter: $popularTitlesFilter\\n first: $first\\n sortBy: $popularTitlesSortBy\\n sortRandomSeed: $sortRandomSeed\\n ) {\\n edges {\\n ...PopularTitleGraphql\\n __typename\\n }\\n pageInfo {\\n startCursor\\n endCursor\\n hasPreviousPage\\n hasNextPage\\n __typename\\n }\\n sponsoredAd {\\n ...SponsoredAdFragment\\n __typename\\n }\\n totalCount\\n __typename\\n }\\n}\\n\\nfragment PopularTitleGraphql on PopularTitlesEdge {\\n cursor\\n node {\\n id\\n objectId\\n objectType\\n content(country: $country, language: $language) {\\n title\\n fullPath\\n scoring {\\n imdbVotes\\n imdbScore\\n tmdbPopularity\\n tmdbScore\\n __typename\\n }\\n posterUrl(profile: $profile, format: $format)\\n ... on ShowContent {\\n backdrops(profile: $backdropProfile, format: $format) {\\n backdropUrl\\n __typename\\n }\\n __typename\\n }\\n isReleased\\n credits(role: DIRECTOR) {\\n name\\n __typename\\n }\\n scoring {\\n imdbVotes\\n __typename\\n }\\n runtime\\n genres {\\n translation(language: $language)\\n __typename\\n }\\n __typename\\n }\\n likelistEntry {\\n createdAt\\n __typename\\n }\\n dislikelistEntry {\\n createdAt\\n __typename\\n }\\n watchlistEntry {\\n createdAt\\n __typename\\n }\\n freeOffersCount: offerCount(\\n country: $country\\n platform: $platform\\n filter: {monetizationTypes: [FREE]}\\n )\\n watchNowOffer(country: $country, platform: $platform, filter: $watchNowFilter) {\\n id\\n standardWebURL\\n package {\\n id\\n packageId\\n clearName\\n __typename\\n }\\n retailPrice(language: $language)\\n retailPriceValue\\n lastChangeRetailPriceValue\\n currency\\n presentationType\\n monetizationType\\n availableTo\\n __typename\\n }\\n ... on Movie {\\n seenlistEntry {\\n createdAt\\n __typename\\n }\\n __typename\\n }\\n ... on Show {\\n seenState(country: $country) {\\n seenEpisodeCount\\n progress\\n __typename\\n }\\n __typename\\n }\\n __typename\\n }\\n __typename\\n}\\n\\nfragment SponsoredAdFragment on SponsoredRecommendationAd {\\n bidId\\n holdoutGroup\\n campaign {\\n externalTrackers {\\n type\\n data\\n __typename\\n }\\n hideRatings\\n promotionalImageUrl\\n watchNowLabel\\n watchNowOffer {\\n standardWebURL\\n presentationType\\n monetizationType\\n package {\\n id\\n packageId\\n shortName\\n clearName\\n icon\\n __typename\\n }\\n __typename\\n }\\n node {\\n id\\n ... on MovieOrShow {\\n content(country: $country, language: $language) {\\n fullPath\\n posterUrl\\n title\\n originalReleaseYear\\n scoring {\\n imdbScore\\n __typename\\n }\\n externalIds {\\n imdbId\\n __typename\\n }\\n backdrops(format: $format, profile: $backdropProfile) {\\n backdropUrl\\n __typename\\n }\\n isReleased\\n __typename\\n }\\n objectId\\n objectType\\n offers(country: $country, platform: $platform) {\\n monetizationType\\n presentationType\\n package {\\n id\\n packageId\\n __typename\\n }\\n id\\n __typename\\n }\\n watchlistEntry {\\n createdAt\\n __typename\\n }\\n __typename\\n }\\n __typename\\n }\\n __typename\\n }\\n __typename\\n}\\n"
}

# Make the POST request
response = httpx.post(url, headers=headers, json=data)

# Check the response status and content
if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=2))  # Print the response JSON data
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)  # Print the response content if it's an error
