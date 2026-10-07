from flask import Flask, request, render_template_string

app = Flask(__name__)

linked_list = []


html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Rainier Chico | Flask Portfolio</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
            line-height: 1.6;
        }

        nav {
            background: #111827;
            padding: 18px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .logo {
            color: white;
            font-size: 22px;
            font-weight: bold;
        }

        .logo span {
            color: #60a5fa;
        }

        .nav-links {
            display: flex;
            gap: 22px;
            flex-wrap: wrap;
        }

        .nav-links a {
            color: #d1d5db;
            text-decoration: none;
            font-size: 14px;
            transition: 0.3s;
        }

        .nav-links a:hover {
            color: #60a5fa;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: 50px auto;
        }

        .hero {
            background: linear-gradient(135deg, #111827, #2563eb);
            color: white;
            padding: 70px 50px;
            border-radius: 25px;
            margin-bottom: 35px;
            box-shadow: 0 15px 35px rgba(37, 99, 235, 0.25);
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .hero h1 span {
            color: #93c5fd;
        }

        .hero p {
            max-width: 650px;
            color: #dbeafe;
            font-size: 18px;
            margin-bottom: 25px;
        }

        .hero-button {
            display: inline-block;
            background: white;
            color: #1d4ed8;
            padding: 12px 22px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .hero-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        }

        .card {
            background: white;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.07);
            margin-bottom: 30px;
        }

        .card h1 {
            font-size: 32px;
            margin-bottom: 10px;
            color: #111827;
        }

        .card h2 {
            color: #2563eb;
            margin: 20px 0 10px;
        }

        .card p {
            color: #6b7280;
            margin-bottom: 12px;
        }

        .section-title {
            text-align: center;
            margin-bottom: 25px;
        }

        .section-title h2 {
            font-size: 30px;
            color: #111827;
        }

        .section-title p {
            color: #6b7280;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .feature {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.06);
            transition: 0.3s;
        }

        .feature:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 25px rgba(0, 0, 0, 0.1);
        }

        .feature-icon {
            font-size: 30px;
            margin-bottom: 12px;
        }

        .feature h3 {
            margin-bottom: 8px;
            color: #111827;
        }

        .feature p {
            color: #6b7280;
            font-size: 14px;
        }

        .feature a {
            display: inline-block;
            margin-top: 10px;
            color: #2563eb;
            text-decoration: none;
            font-weight: bold;
        }

        .profile-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
            align-items: center;
        }

        .profile-box {
            background: linear-gradient(135deg, #2563eb, #1e40af);
            color: white;
            padding: 40px;
            border-radius: 18px;
            text-align: center;
        }

        .profile-circle {
            width: 120px;
            height: 120px;
            background: white;
            color: #2563eb;
            border-radius: 50%;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 42px;
            font-weight: bold;
        }

        .profile-box h2 {
            color: white;
        }

        .profile-box p {
            color: #dbeafe;
        }

        .info {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-top: 20px;
        }

        .info-box {
            background: #f8fafc;
            padding: 18px;
            border-radius: 10px;
            border-left: 4px solid #2563eb;
        }

        .info-box strong {
            display: block;
            color: #111827;
            margin-bottom: 5px;
        }

        .info-box span {
            color: #6b7280;
            font-size: 14px;
        }

        form {
            margin-top: 25px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 7px;
            color: #374151;
        }

        input {
            width: 100%;
            padding: 13px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            margin-bottom: 15px;
            font-size: 15px;
            outline: none;
            transition: 0.3s;
        }

        input:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            margin: 5px 3px;
            transition: 0.3s;
        }

        button:hover {
            background: #1d4ed8;
            transform: translateY(-2px);
        }

        .result {
            margin-top: 25px;
            padding: 20px;
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 10px;
            color: #1e40af;
        }

        .result-title {
            font-weight: bold;
            margin-bottom: 5px;
        }

        .formula {
            background: #f8fafc;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #2563eb;
        }

        .linked-list {
            margin-top: 25px;
        }

        .list-item {
            display: inline-block;
            background: #2563eb;
            color: white;
            padding: 12px 18px;
            border-radius: 8px;
            margin: 5px;
            font-weight: bold;
            position: relative;
        }

        .list-item:not(:last-child)::after {
            content: " →";
            color: #9ca3af;
            position: absolute;
            right: -28px;
        }

        .empty {
            background: #f3f4f6;
            color: #6b7280;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .contact-box {
            padding: 25px;
            background: #f8fafc;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
        }

        .contact-box h3 {
            color: #2563eb;
            margin-bottom: 8px;
        }

        .contact-box p {
            margin: 0;
        }

        footer {
            background: #111827;
            color: #9ca3af;
            text-align: center;
            padding: 30px;
            margin-top: 60px;
        }

        footer strong {
            color: white;
        }

        @media (max-width: 800px) {
            nav {
                flex-direction: column;
                gap: 15px;
            }

            .hero h1 {
                font-size: 36px;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .profile-grid {
                grid-template-columns: 1fr;
            }

            .info {
                grid-template-columns: 1fr;
            }

            .contact-grid {
                grid-template-columns: 1fr;
            }
        }

    </style>
</head>

<body>

    <nav>
        <div class="logo">
            Chicodes<span>.</span>
        </div>

        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/profile">Profile</a>
            <a href="/uppercase">Uppercase</a>
            <a href="/circle">Circle</a>
            <a href="/triangle">Triangle</a>
            <a href="/linked-list">Linked List</a>
            <a href="/contact">Contact</a>
        </div>
    </nav>


    <div class="container">

        {% if page == "home" %}

        <section class="hero">
            <h1>Hello, I'm <span>Rainier Chico</span></h1>

            <p>
                A Computer Engineering student exploring in programming,
                web development, and technology using Python Flask.
            </p>

            <a href="/profile" class="hero-button">
                View My Profile
            </a>
        </section>


        <div class="section-title">
            <h2>My Programming Works</h2>
            <p>Explore the programs included in this Flask project.</p>
        </div>

        <div class="grid">

            <div class="feature">
                <div class="feature-icon">🔤</div>
                <h3>Uppercase Converter</h3>
                <p>
                    Convert any word or sentence into uppercase letters.
                </p>
                <a href="/uppercase">Try it →</a>
            </div>

            <div class="feature">
                <div class="feature-icon">⭕</div>
                <h3>Circle Calculator</h3>
                <p>
                    Calculate the area of a circle using its radius.
                </p>
                <a href="/circle">Try it →</a>
            </div>

            <div class="feature">
                <div class="feature-icon">🔺</div>
                <h3>Triangle Calculator</h3>
                <p>
                    Calculate the area of a triangle using base and height.
                </p>
                <a href="/triangle">Try it →</a>
            </div>

            <div class="feature">
                <div class="feature-icon">🔗</div>
                <h3>Linked List</h3>
                <p>
                    Add, delete, and search values using a linked list.
                </p>
                <a href="/linked-list">Try it →</a>
            </div>

            <div class="feature">
                <div class="feature-icon">👨‍💻</div>
                <h3>Profile</h3>
                <p>
                    Learn more about me and my Computer Engineering journey.
                </p>
                <a href="/profile">View profile →</a>
            </div>

            <div class="feature">
                <div class="feature-icon">📧</div>
                <h3>Contact</h3>
                <p>
                    View my contact information and school details.
                </p>
                <a href="/contact">Contact me →</a>
            </div>

        </div>


        {% elif page == "profile" %}

        <div class="card">

            <div class="profile-grid">

                <div class="profile-box">

                    <div class="profile-circle">
                        RC
                    </div>

                    <h2>Rainier Chico</h2>

                    <p>
                        Computer Engineering 
                    </p>

                </div>

                <div>

                    <h1>About Me</h1>

                    <p>
                        Hello! I'm Rainier Chico, a Computer Engineering
                        student interested in harwares, programming, computers,
                        technology, and web development.
                    </p>

                    <p>
                        This website demonstrates some of the programming
                        concepts I have learned using Python and Flask.
                    </p>

                    <div class="info">

                        <div class="info-box">
                            <strong>Course</strong>
                            <span>BS Computer Engineering</span>
                        </div>

                        <div class="info-box">
                            <strong>School</strong>
                            <span>Polytechnic University of the Philippines</span>
                        </div>

                        <div class="info-box">
                            <strong>Year Level</strong>
                            <span>2nd Year</span>
                        </div>

                        <div class="info-box">
                            <strong>Interests</strong>
                            <span>Web Development and Hardware</span>
                        </div>

                    </div>

                </div>

            </div>

        </div>


        {% elif page == "uppercase" %}

        <div class="card">

            <h1>Uppercase Converter</h1>

            <p>
                Enter any word or sentence and convert it into uppercase.
            </p>

            <form method="POST">

                <label>Enter text</label>

                <input
                    type="text"
                    name="text"
                    placeholder="Example: hello world"
                    required
                >

                <button type="submit">
                    Convert to Uppercase
                </button>

            </form>

            {% if result %}

            <div class="result">

                <div class="result-title">
                    Result
                </div>

                <p>
                    {{ result }}
                </p>

            </div>

            {% endif %}

        </div>


        {% elif page == "circle" %}

        <div class="card">

            <h1>Area of a Circle</h1>

            <p>
                Calculate the area of a circle by entering its radius.
            </p>

            <div class="formula">
                A = πr²
            </div>

            <form method="POST">

                <label>Radius</label>

                <input
                    type="number"
                    name="radius"
                    step="any"
                    placeholder="Enter radius"
                    required
                >

                <button type="submit">
                    Calculate Area
                </button>

            </form>

            {% if result %}

            <div class="result">

                <div class="result-title">
                    Calculated Area
                </div>

                <p>
                    {{ "%.2f"|format(result) }} square units
                </p>

            </div>

            {% endif %}

        </div>


        {% elif page == "triangle" %}

        <div class="card">

            <h1>Area of a Triangle</h1>

            <p>
                Calculate the area of a triangle using its base and height.
            </p>

            <div class="formula">
                A = ½ × base × height
            </div>

            <form method="POST">

                <label>Base</label>

                <input
                    type="number"
                    name="base"
                    step="any"
                    placeholder="Enter base"
                    required
                >

                <label>Height</label>

                <input
                    type="number"
                    name="height"
                    step="any"
                    placeholder="Enter height"
                    required
                >

                <button type="submit">
                    Calculate Area
                </button>

            </form>

            {% if result %}

            <div class="result">

                <div class="result-title">
                    Calculated Area
                </div>

                <p>
                    {{ "%.2f"|format(result) }} square units
                </p>

            </div>

            {% endif %}

        </div>


        {% elif page == "linkedlist" %}

        <div class="card">

            <h1>Linked List</h1>

            <p>
                Use the buttons below to add, delete, or search
                for values in the linked list.
            </p>

            <form method="POST">

                <label>Value</label>

                <input
                    type="text"
                    name="value"
                    placeholder="Enter a value"
                    required
                >

                <button
                    type="submit"
                    name="action"
                    value="add">
                    Add
                </button>

                <button
                    type="submit"
                    name="action"
                    value="delete">
                    Delete
                </button>

                <button
                    type="submit"
                    name="action"
                    value="search">
                    Search
                </button>

            </form>

            {% if message %}

            <div class="result">
                {{ message }}
            </div>

            {% endif %}

            <div class="linked-list">

                <h2>Current Linked List</h2>

                {% if linked_list %}

                    {% for item in linked_list %}

                    <span class="list-item">
                        {{ item }}
                    </span>

                    {% endfor %}

                {% else %}

                    <div class="empty">
                        The linked list is currently empty.
                    </div>

                {% endif %}

            </div>

        </div>


        {% elif page == "contact" %}

        <div class="card">

            <h1>Contact Me</h1>

            <p>
                Here are my contact and school details.
            </p>

            <div class="contact-grid">

                <div class="contact-box">
                    <h3>👤 Name</h3>
                    <p>Rainier Chico</p>
                </div>

                <div class="contact-box">
                    <h3>📧 Email</h3>
                    <p>raingaming016@gmail.com</p>
                </div>

                <div class="contact-box">
                    <h3>📱 Phone</h3>
                    <p>0999 775 0898</p>
                </div>

                <div class="contact-box">
                    <h3>💻 GitHub</h3>
                    <p>raingaming016-dot</p>
                </div>

                <div class="contact-box">
                    <h3>🎓 School</h3>
                    <p>Polytechnic University of the Philippines</p>
                </div>

                <div class="contact-box">
                    <h3>💻 Course</h3>
                    <p>BS Computer Engineering</p>
                </div>

            </div>

        </div>

        {% endif %}

    </div>


    <footer>

        <p>
            © 2026 <strong>Rainier Chico</strong>
        </p>

        <p>
            Built with Python Flask
        </p>

    </footer>

</body>

</html>
"""


@app.route("/")
def home():
    return render_template_string(
        html,
        page="home"
    )


@app.route("/profile")
def profile():
    return render_template_string(
        html,
        page="profile"
    )


@app.route("/contact")
def contact():
    return render_template_string(
        html,
        page="contact"
    )


@app.route("/uppercase", methods=["GET", "POST"])
def uppercase():
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        result = text.upper()

    return render_template_string(
        html,
        page="uppercase",
        result=result
    )


@app.route("/circle", methods=["GET", "POST"])
def circle():
    result = ""

    if request.method == "POST":
        radius = float(request.form.get("radius", 0))

        if radius >= 0:
            result = 3.14 * radius * radius

    return render_template_string(
        html,
        page="circle",
        result=result
    )


@app.route("/triangle", methods=["GET", "POST"])
def triangle():
    result = ""

    if request.method == "POST":
        base = float(request.form.get("base", 0))
        height = float(request.form.get("height", 0))

        if base >= 0 and height >= 0:
            result = 0.5 * base * height

    return render_template_string(
        html,
        page="triangle",
        result=result
    )


@app.route("/linked-list", methods=["GET", "POST"])
def linkedlist():
    message = ""

    if request.method == "POST":

        action = request.form.get("action")
        value = request.form.get("value", "").strip()

        if action == "add":

            linked_list.append(value)
            message = value + " was added to the linked list."

        elif action == "delete":

            if value in linked_list:
                linked_list.remove(value)
                message = value + " was deleted from the linked list."
            else:
                message = value + " was not found."

        elif action == "search":

            if value in linked_list:
                message = value + " was found in the linked list."
            else:
                message = value + " was not found."

    return render_template_string(
        html,
        page="linkedlist",
        linked_list=linked_list,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)