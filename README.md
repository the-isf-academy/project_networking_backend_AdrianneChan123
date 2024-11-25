# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
My API is an interactive platform designed for kpop lovers. It displays different kpop artist profiles, ranging from boy groups to girl groups. Not only you will be able to access the basic information about various kpop artists, you will also be able to view the most updated rankings of the artists, their generated popularity, as well as comments from other users. Generally, this API contains a wide variety of information on kpop artists, please go ahead and take your time to explore this API!

### Model
| Method name          | Parameters        | Related fields | Field data type           | What it does                                                                         |
|----------------------|-------------------|----------------|---------------------------|--------------------------------------------------------------------------------------|
| json_response        | self              | all fields     | string, integer and float | returns the information of the kpop profile in a json response                       |
| renew_comment        | self, new_comment | comment        | string                    | updates the comment of the corresponding kpop profile to the most newly inputted one |
| increase_likes       | self              | likes          | integer                   | increases the likes of the kpop profile by 1                                         |
| increase_views       | self              | views          | integer                   | increases the views of the kpop profile by 1                                         |
| calculate_popularity | self              | popularity     | float                     | calculates the percentage of popularity using the fields likes and views             |

### Endpoints
| Route name     | HTTP Method | Payload                                                                   | What it does                                                                                                          |
|----------------|-------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| all            | get         | none                                                                      | gets all of the kpop profiles                                                                                         |
| random         | get         | none                                                                      | displays a random kpop profile                                                                                        |
| one            | get         | artist_name                                                               | displays the user's chosen kpop profile                                                                               |
| new            | post        | artist_name, debut, members, fandom_name, fandom_colour, company, comment | allows the user to add a new kpop profile to the API                                                                  |
| likes          | post        | artist_name                                                               | allows the user to like the kpop artist that they admire                                                              |
| search_company | get         | company                                                                   | queries the profiles of kpop artists under the specific company only                                                  |
| change_comment | post        | artist_name, new_comment                                                  | allows the user to comment on kpop artist profiles, which the new comment will automatically replace the previous one |
| top_5          | get         | none                                                                      | shows a most updated podium of the top 5 artists with the most likes                                                  |
| rankings       | get         | none                                                                      | presents a general ranking of the kpop artists, according to their number of likes                                    |

---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)

BASE_URL = "http://127.0.0.1:5000/kpop_profiles/"



