from flask import Flask, jsonify, request
import csv
from demographic import output
from storage import all_movie, liked_movies, did_not_match, not_liked
from contentBased import getMovieRecommendation

app = Flask(__name__)
# @app.route("/getMovies")
# def getMovies():
#     return jsonify({
#         "data":all_movie[0],
#         "status":"success"
#     })


@app.route("/getMovie")
def getMovies():
    movie_data = {
        "title": all_movie[0][8],
        "posterlink": all_movie[0][27],
        "release_date": all_movie[0][13],
        "duration": all_movie[0][15],
        "rating": all_movie[0][20],
        "overview": all_movie[0][9],
    }
    return jsonify({
        "movie_data": movie_data,
        "status": "SUCCESS"
    })


@app.route("/likedMovies", methods=["POST"])
def likedMovies():
    movie = all_movie[0]
    liked_movies.append(movie)
    all_movie.pop(0)
    return jsonify({
        "status": "success"
    })


@app.route("/didnotlikeMovies", methods=["POST"])
def didnot_likedMovies():
    movie = all_movie[0]
    did_not_match.append(movie)
    all_movie.pop(0)
    return jsonify({
        "status": "success"
    })


@app.route("/didnot", methods=["POST"])
def not_matched_Movies():
    movie = all_movie[0]
    not_liked.append(movie)
    all_movie.pop(0)
    return jsonify({
        "status": "success"
    })


@app.route("/popularMovies")
def popularMovies():
    movie_data = []
    for i in output:
        d = {
            "title": i[0],
            "posterlink": i[1],
            "release_date": i[2],
            "duration": i[3],
            "rating": i[4],
            "overview": i[5],
        }
        movie_data.append(d)
    return jsonify({
        "movie_data": movie_data,
        "status": "SUCCESS"
    })


@app.route("/recommendation")
def recommendation():
    recommendedMoives = []
    for i in liked_movies:
        output = getMovieRecommendation(i[8])
        for j in output:
            recommendedMoives.append(j)
    import itertools
    recommendedMoives.sort()
    recommendedMoives = list(recommendedMoives for recommendedMoives,_ in itertools.groupby(recommendedMoives))
    movie_data = []
    for i in recommendedMoives:
        d = {
            "title": i[0],
            "posterlink": i[1],
            "release_date": i[3],
            "duration": i[2],
            "rating": i[4],
            "overview": i[5],

        }
        movie_data.append(d)
    return jsonify({
        "movie_data":movie_data,
        "status":"success"
    })        


if __name__ == "__main__":
    app.run()
