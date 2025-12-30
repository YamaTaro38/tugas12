from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Data anggota kelompok
team_members = [
    {
        'name': 'Faqih Abdullah',
        'nim': '2311102048',
        'role': 'Anggota Kelompok'
    },
    {
        'name': 'M Daffa Bagus J',
        'nim': '2311102222',
        'role': 'Anggota Kelompok'
    },
    {
        'name': 'M Rafiful Hana',
        'nim': '2311102227',
        'role': 'Anggota Kelompok'
    }
]

# Data tugas
tasks = [
    {
        'id': 1,
        'title': 'Carilah penyedia PaaS yang free!',
        'description': 'Mencari dan mengevaluasi penyedia Platform as a Service (PaaS) yang menawarkan layanan gratis untuk deployment aplikasi.',
        'status': 'Completed'
    },
    {
        'id': 2,
        'title': 'Buatlah aplikasi sederhana menggunakan layanan PaaS tersebut!',
        'description': 'Membuat aplikasi web sederhana menggunakan Flask dan melakukan deployment ke penyedia PaaS gratis yang telah dipilih.',
        'status': 'Completed'
    }
]

# Data penyedia PaaS gratis
paas_providers = [
    {
        'name': 'Railway',
        'description': 'Platform deployment modern dengan free tier yang murah hati',
        'features': ['Free $5 credit monthly', 'Deployment otomatis dari GitHub', 'Database included'],
        'link': 'https://railway.app'
    },
    {
        'name': 'Render',
        'description': 'Platform cloud untuk static sites dan web services',
        'features': ['Free tier untuk web services', 'Deployment otomatis', 'SSL gratis'],
        'link': 'https://render.com'
    },
    {
        'name': 'Heroku',
        'description': 'Pioneer dalam platform PaaS dengan ecosystem yang besar',
        'features': ['Free dynos terbatas', 'Add-ons ecosystem', 'Easy deployment'],
        'link': 'https://heroku.com'
    },
    {
        'name': 'PythonAnywhere',
        'description': 'Platform hosting khusus untuk aplikasi Python',
        'features': ['Free tier untuk aplikasi web', 'Python environment', 'Terminal access'],
        'link': 'https://pythonanywhere.com'
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                         team_members=team_members, 
                         tasks=tasks,
                         paas_providers=paas_providers)

@app.route('/team')
def team():
    return render_template('index.html', 
                         team_members=team_members, 
                         tasks=tasks,
                         paas_providers=paas_providers,
                         section='team')

@app.route('/tasks')
def tasks_page():
    return render_template('index.html', 
                         team_members=team_members, 
                         tasks=tasks,
                         paas_providers=paas_providers,
                         section='tasks')

@app.route('/paas')
def paas():
    return render_template('index.html', 
                         team_members=team_members, 
                         tasks=tasks,
                         paas_providers=paas_providers,
                         section='paas')

@app.route('/deployment')
def deployment():
    return render_template('index.html', 
                         team_members=team_members, 
                         tasks=tasks,
                         paas_providers=paas_providers,
                         section='deployment')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Di sini Anda bisa menambahkan logika untuk menyimpan atau mengirim email
    print(f"Pesan dari {name} ({email}): {message}")
    
    return redirect(url_for('index', message_sent=True))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5500))
    app.run(host='0.0.0.0', port=port, debug=True)