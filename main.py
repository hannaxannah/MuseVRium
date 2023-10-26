from flask import Flask, request, jsonify, render_template, redirect, url_for
import json
import os
from scipy.spatial import distance

app = Flask(__name__)

# JSON 파일에서 명화의 색상 정보를 읽어오기
with open('colors_data.json', 'r', encoding='utf-8') as file:
    paintings_colors = json.load(file)

# JSON 파일에서 사용자가 선택할 수 있는 선호 색상 정보를 읽어오기
with open('image_colors.json', 'r', encoding='utf-8') as file:
    image_colors = json.load(file)

# JSON 파일에서 사용자가 선택할 수 있는 싫어하는 색상 정보를 읽어오기
with open('least_used_colors.json', 'r', encoding='utf-8') as file:
    least_used_colors = json.load(file)

def calculate_rgb_distance(color1, color2):
    return distance.euclidean(color1, color2)

def compare_paintings_with_user_choice(paintings_colors, user_liked_colors, user_disliked_color):
    best_score = float('-inf')
    best_painting = None

    for painting, colors in paintings_colors.items():
        score = 0
        for user_color in user_liked_colors:
            score += sum([1 / (calculate_rgb_distance(user_color, painting_color) + 1) for painting_color in colors['liked_colors']])
        disliked_distance = calculate_rgb_distance(user_disliked_color, colors.get('disliked_color', [0, 0, 0]))
        score -= disliked_distance
        if score > best_score:
            best_score = score
            best_painting = painting

    return best_painting


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/select')
def select():
    return render_template('main.html')


@app.route('/result', methods=['POST'])
def result():
    liked_colors = request.form.get('liked_colors')
    disliked_color = request.form.get('disliked_color')

    liked_rgb_values = [image_colors[color] for color in liked_colors.split(",")]
    disliked_rgb_value = least_used_colors[disliked_color]

    recommended_painting = compare_paintings_with_user_choice(paintings_colors, liked_rgb_values, disliked_rgb_value)

    # 명화 데이터 추출 from colors_data.json
    painting_info = paintings_colors[recommended_painting]
    title = painting_info["title"]
    artist = painting_info["artist"]
    description = painting_info["description"]
    vr_link = painting_info["vr_link"]
    original_image = painting_info["original_image"]
    color_image = painting_info["color_image"]

    return render_template('result.html', title=title, artist=artist, description=description, vr_link=vr_link, original_image=original_image, color_image=color_image)

if __name__ == '__main__':
    app.run(debug=True)
