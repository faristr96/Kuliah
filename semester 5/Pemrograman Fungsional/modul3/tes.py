import os
os.system('cls' if os.name == 'nt' else 'clear')

movies = [
    {"title" : "Avanger: Endgame", "year": 2019, "rating":8.4, "genre": "Action"},
    {"title" : "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title" : "Nomadlan", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title" : "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title" : "Spider-Man", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title" : "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title" : "A Quiet place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title" : "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title" : "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title" : "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title" : "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def show_movie_data(movie_title):
    selected_movie = list(filter(lambda x: x["title"] == movie_title, movies))
    if selected_movie:
        movie_info = list(map(lambda x: {"title": x["title"], "year": x["year"], "rating": x["rating"], "genre": x["genre"]}, selected_movie))
        print(f"\nInformasi Film: {movie_info[0]['title']}")
        print(f"Rating: {movie_info[0]['rating']}")
        print(f"Tahun Rilis: {movie_info[0]['year']}")
        print(f"Genre: {movie_info[0]['genre']}")
    else:
        print("Film tidak ditemukan.")

def count_movies_by_genre():
    genre_count = {}
    for movie in movies:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count
  
def average_rating_by_year():
    rating_by_year = {}
    count_by_year = {}
    for movie in movies:
        year = movie["year"]
        rating = movie["rating"]
        rating_by_year[year] = rating_by_year.get(year, 0) + rating
        count_by_year[year] = count_by_year.get(year, 0) + 1
        average_rating = {year: rating / count_by_year[year] for year, rating in rating_by_year.items()}
    return average_rating

def highest_rated_movie():
    highest_rated = max(movies, key=lambda x: x["rating"])
    return highest_rated

while True:
    print("Pilih tugas yang ingin dilakukan: \n")
    print("1. Menampilkan data film yang dipilih")
    print("2. Jumlah film berdasarkan genre")
    print("3. Rata-rata rating film berdasarkan tahun rilis")
    print("4. Film dengan rating tertinggi\n")
    print("5. Selesai")
    menu = int(input('Masukan nomor tugas (1/2/3/4/5): '))

    
    if menu == 1:
        title = str(input("Masukan judul film yang ingin dicari: "))
        print(show_movie_data(title))
    elif menu == 2:
        print(count_movies_by_genre())
        print("\n")
    elif menu == 3:
        print(average_rating_by_year())
        print("\n")
    elif menu == 4:
        print(f"Informasi Film: {highest_rated_movie()['title']}")
        print(f"Rating: {highest_rated_movie()['rating']}")
        print(f"Tahun Rilis: {highest_rated_movie()['year']}")
        print(f"Genre: {highest_rated_movie()['genre']}\n")
    elif menu == 5:
        break