# AWWWARDS
*BY OKALL VIVIAN*

## Description

This is a simple application where one can submit,rate and look at people's sites.


## User Stories
Through this application a user is able to:

1. View posted projects and their details


2. Post a project to be rated/reviewed


3. Rate/ review other users' projects


4. Search for projects 


5. View projects overall score


6. View my profile page


## Setup/Installation Requirements
To start using this project use the following commands:

* `git clone https://github.com/Okalll/Awwwwards.git`

* `cd Awwwards`

* `atom .`

* `code . `(this is if Visual Studio Code is your preferred text editor)

To run this program

* run this command lines in your terminal:

* `python manage.py runserver`

* access the application on this localhost address `http://127.0.0.1:8000`


## Prerequisites

You need the following to work on the project:

`-Python version 3.6`

`-Django 1.11.5`

`-Pip`

`virtual`environment

`-A text  Editor`


##Behaviour Driven Development

|  Behaviour |  Input  |  Output |
|------------|---------|---------|
| The program should displays the sign-up form first | credentials of the user | A user is created |
| The program authenticates the user first before anything else  | One is required to login/signup | Redirected to log-in again for proper authentication |
|The program should direct the user to their timeline page when logged in | Login as a user | Redirected to the timeline page with photos posted by other users |
|The program should have a rate it button | Click on the rate it button | you are prompted to rate in various categories|
|The program should have a comment section on a site | Write on the comment section | The comment will appear on the submitted site| 

## Link to Live Website



## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

## License
MIT License

Copyright (c) 2018 Okall Vivian

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.