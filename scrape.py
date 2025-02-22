from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import csv

# Headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}

names = []
ratings = []
reviews = []
price_features = []
price_features_ratings = [] 
design_features = []
design_features_ratings = []
practility_features = []
practility_features_ratings = []
under_bonnet_features = [] 
under_bonnet_features_ratings = []
efficiency_features = [] 
efficiency_features_ratings = []
driving_features = [] 
driving_features_ratings = [] 
safety_features = [] 
safety_features_ratings = []
ownership_features = []
ownership_features_ratings = []
url_ratings = []
keep = True 

for i in range(1, 200):
    url = "https://www.carsguide.com.au/articles/car-reviews?page=" + str(i)

    # Function to fetch the HTML content with retries
    def fetch_html(url, headers, retries=3):
        for i in range(retries):
            try:
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()  # Raise an exception for HTTP errors
                return response.text
            except requests.exceptions.RequestException as e:
                print(f"Attempt {i+1} failed: {e}")
                time.sleep(0)  # Wait before retrying
        return None

    # Fetch the HTML content
    html_content = fetch_html(url, headers)

    if html_content:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        
        for x in range(1,20):
            boolean = "even" if x % 2 == 0 else "odd"
            keep = True
            views_row = soup.find("div", class_="view-content")

            if(x == 1): 
                view_single_row = soup.find("div", class_="view-content").find("div", class_="views-row views-row-"+ str(x) + " views-row-" +str(boolean) + " views-row-first").find("div", class_="media").find("div", class_="media-body").find("a")
                name = view_single_row.get_text()
            else: 
                view_single_row = soup.find("div", class_="view-content").find("div", class_="views-row views-row-"+ str(x) + " views-row-" +str(boolean)).find("div", class_="media").find("div", class_="media-body").find("a")
                name = view_single_row.get_text()

            body = view_single_row
            url_rating = "https://www.carsguide.com.au" + view_single_row.get("href")
            print(url_rating)
            fetch_html(url_rating, headers)
            soup_rating = BeautifulSoup(fetch_html(url_rating, headers), "html.parser")
            rating = soup_rating.find("div", class_="bg-purple-20 px-12px min-w-[30px] py-8px font-bold rounded-4px align-middle self-end text-heading-02-mob m:text-heading-02 text-center")
            general_review = soup_rating.find("div", class_="article-content")
            

            # Print the body and rating

            if not name.__contains__("snapshot"):
                if name and rating:
                    print(name)
                    print(rating.text)


                    h2_tags = general_review.find_all("h2", class_="flex gap-16px mb-0")
                    price_features_ratings_aux = []
                    design_features_ratings_aux = []
                    practility_features_ratings_aux = []
                    under_bonnet_features_ratings_aux = []
                    efficiency_features_ratings_aux = []
                    driving_features_ratings_aux = []
                    safety_features_ratings_aux = []
                    ownership_features_ratings_aux = []
                    price_features_aux = []
                    design_features_aux = []
                    practility_features_aux = []
                    under_bonnet_features_aux = []
                    efficiency_features_aux = []
                    driving_features_aux = []
                    safety_features_aux = []
                    ownership_features_aux = []
                    for i in range(len(h2_tags) - 1):
                        match i: 
                            case 0:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux:
                                    price_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 1:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux : 
                                    design_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 2:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux: 
                                    practility_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 3:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux: 
                                    under_bonnet_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 4:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux: 
                                    efficiency_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 5:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux: 
                                    driving_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 6:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux: 
                                    safety_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False
                            case 7:
                                aux = h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")
                                if aux: 
                                    ownership_features_ratings_aux.append(h2_tags[i].find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                else: 
                                    keep = False

                        if keep == True:
                            h2_tag = h2_tags[i]
                            next_h2_tag = h2_tags[i + 1]

                            # Find all 'p' tags between h2_tag and next_h2_tag
                            p_tags = []
                            for sibling in h2_tag.next_siblings:
                                if sibling == next_h2_tag:
                                    break
                                if sibling.name == 'p':
                                    p_tags.append(sibling)

                            for p in p_tags:
                                match i: 
                                    case 0: 
                                        price_features_aux.append(p.get_text())
                                    case 1:
                                        design_features_aux.append(p.get_text())
                                    case 2:
                                        practility_features_aux.append(p.get_text())
                                    case 3:
                                        under_bonnet_features_aux.append(p.get_text())
                                    case 4:
                                        efficiency_features_aux.append(p.get_text())
                                    case 5:
                                        driving_features_aux.append(p.get_text())
                                    case 6:
                                        safety_features_aux.append(p.get_text())

                        
                    if (keep == True and len(h2_tags) > 0):
                            # Handle the last h2 tag separately
                            last_h2_tag = h2_tags[7]
                            p_tags = []
                            for sibling in last_h2_tag.next_siblings:
                                if sibling.name == 'p':
                                    p_tags.append(sibling)
                            if(last_h2_tag.find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end")):
                                ownership_features_ratings_aux.append(last_h2_tag.find("div", class_="bg-purple-20 pr-8px pl-8px pt-4px pb-4px font-bold flex-shrink-0 rounded-4px align-middle self-end").get_text())
                                names.append(name)
                                ratings.append(rating.text)
                                url_ratings.append(url_rating)
                            else: 
                                keep = False
                                break
                            if(price_features_ratings_aux != []):
                                price_features_ratings.append(price_features_ratings_aux)
                                price_features.append(price_features_aux)
                            else: 
                                break
                            if(design_features_ratings_aux != []):
                                design_features_ratings.append(design_features_ratings_aux)
                                design_features.append(design_features_aux)
                            else: 
                                break
                            if(practility_features_ratings_aux != []):
                                practility_features_ratings.append(practility_features_ratings_aux)
                                practility_features.append(practility_features_aux)
                            else:
                                break
                            if(under_bonnet_features_ratings_aux != []):
                                under_bonnet_features_ratings.append(under_bonnet_features_ratings_aux)
                                under_bonnet_features.append(under_bonnet_features_aux)
                            else:
                                break
                            if(efficiency_features_ratings_aux != []):
                                efficiency_features_ratings.append(efficiency_features_ratings_aux)
                                efficiency_features.append(efficiency_features_aux)
                            else: 
                                break
                            if(driving_features_ratings_aux != []):
                                driving_features_ratings.append(driving_features_ratings_aux)
                                driving_features.append(driving_features_aux)
                            else:
                                break
                            if(safety_features_ratings_aux != []):
                                safety_features_ratings.append(safety_features_ratings_aux)
                                safety_features.append(safety_features_aux)
                            else:
                                break
                            if(ownership_features_ratings_aux != []):
                                ownership_features_ratings.append(ownership_features_ratings_aux)
                                ownership_features.append(p_tags)
                            else:
                                break

        
    
    else:
        print("Failed to retrieve the HTML content.")

# Print the lengths of all lists
print(f"names: {len(names)}")
print(f"ratings: {len(ratings)}")
print(f"price_features: {len(price_features)}")
print(f"price_features_ratings: {len(price_features_ratings)}")
print(f"design_features: {len(design_features)}")
print(f"design_features_ratings: {len(design_features_ratings)}")
print(f"practility_features: {len(practility_features)}")
print(f"practility_features_ratings: {len(practility_features_ratings)}")
print(f"under_bonnet_features: {len(under_bonnet_features)}")
print(f"under_bonnet_features_ratings: {len(under_bonnet_features_ratings)}")
print(f"efficiency_features: {len(efficiency_features)}")
print(f"efficiency_features_ratings: {len(efficiency_features_ratings)}")
print(f"driving_features: {len(driving_features)}")
print(f"driving_features_ratings: {len(driving_features_ratings)}")
print(f"safety_features: {len(safety_features)}")
print(f"safety_features_ratings: {len(safety_features_ratings)}")
print(f"ownership_features: {len(ownership_features)}")
print(f"ownership_features_ratings: {len(ownership_features_ratings)}")



# Define the header for the CSV file
header = [
    "Name", "Rating", "Price Feature Rating", "Price Feature", "Design Feature", "Design Feature Rating",
    "Practicality Feature", "Practicality Feature Rating", "Under Bonnet Feature", "Under Bonnet Feature Rating",
    "Efficiency Feature", "Efficiency Feature Rating", "Driving Feature", "Driving Feature Rating",
    "Safety Feature", "Safety Feature Rating", "Ownership Feature", "Ownership Feature Rating", "URL"
]

# Save in a csv file carsguide_scrape.csv
with open("carsguide_scrape.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header

    min_length = min(
        len(names), len(ratings), len(price_features_ratings), len(price_features), len(design_features),
        len(design_features_ratings), len(practility_features), len(practility_features_ratings),
        len(under_bonnet_features), len(under_bonnet_features_ratings), len(efficiency_features),
        len(efficiency_features_ratings), len(driving_features), len(driving_features_ratings),
        len(safety_features), len(safety_features_ratings), len(ownership_features), len(ownership_features_ratings)
    )

    for i in range(min_length):
        row = [
            names[i], ratings[i], price_features_ratings[i], price_features[i], design_features[i],
            design_features_ratings[i], practility_features[i], practility_features_ratings[i],
            under_bonnet_features[i], under_bonnet_features_ratings[i], efficiency_features[i],
            efficiency_features_ratings[i], driving_features[i], driving_features_ratings[i],
            safety_features[i], safety_features_ratings[i], ownership_features[i], ownership_features_ratings[i],url_ratings[i]
        ]
        writer.writerow(row)  # Write the row
