import time
import pygame
from rich.console import Console
from rich.table import Table
from rich.text import Text
from datetime import datetime
import random
from assets.banner import print_professor_banner
from assets.html_data import read_html_data

console = Console()

# مسار الصوت
BIRD_SOUND_PATH = "assets/sounds/owl_sound.mp3"  # حط مسار الصوت هنا

# وظيفة تشغيل الصوت
def play_bird_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(BIRD_SOUND_PATH)
    pygame.mixer.music.play()

# دالة لتوليد IP عشوائي مصري
def generate_random_ip():
    # اختر أحد النطاقات المصرية الممكنة
    ip_range = ['41.', '156.']
    
    # اختر نطاق عشوائي من النطاقات المصرية
    ip_prefix = random.choice(ip_range)
    
    # توليد بقية الأرقام بشكل عشوائي من 0 لـ 255
    ip = f"{ip_prefix}{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    return ip

def start_tool():
    print_professor_banner()
    play_bird_sound()
    
    phone_number = input("Enter phone number: ")
    country_code = input("Enter country code: ")

    console.print(f"[bold red]Initializing... Loading [red]{phone_number}[/red] in {country_code}...[/bold red]")

    loading_bar()

    html_file = f"assets/html_data/{phone_number}_{country_code}_data.html"
    data = read_html_data(html_file)

    console.print(f"\n[bold yellow]Connecting to {phone_number}... Please wait...[/bold yellow]")
    time.sleep(10)
    console.print(f"[bold green]Connection Established![/bold green]")
    
    time.sleep(1)
    console.print(f"[bold yellow]Gathering information... Please wait...[/bold yellow]")
    time.sleep(5)

    display_results(data)

def loading_bar():
    console.print("[bold yellow]Preparing for recon...[/bold yellow]")
    for i in range(10):
        time.sleep(0.5)
        console.print(f"[bold white]Loading: {i*10}%[/bold white]")
    console.print(f"[bold red]Loading Complete... Ready to Hack![/bold red]\n")

def display_results(data):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    random_ip = generate_random_ip()  # توليد IP عشوائي مصري

    table = Table(title=f"[bold red]Recon Results for {phone_number}[/bold red]", show_header=True, header_style="bold green")
    table.add_column("Date/Time", style="dim", width=20)
    table.add_column("Action", style="bold yellow")
    table.add_column("Details", style="bold white")

    table.add_row(current_time, "Accessing Google History", "Visited: google.com at 2025-05-07 10:00")
    table.add_row(current_time, "Tracking Location", f"Detected IP: {random_ip}")  # عرض الـ IP العشوائي
    table.add_row(current_time, "Reading History", "Visited: example.com at 2025-05-07 10:30")
    
    table.add_row(current_time, "Analysis Completed", data)

    console.print(table)

    results = data.split("\n")
    chunk_size = 5 

    for i in range(0, len(results), chunk_size):
        time.sleep(5)
        console.print(f"\n[bold green]Displaying Results {i+1} to {min(i+chunk_size, len(results))}[/bold green]")
        for line in results[i:i+chunk_size]:
            console.print(f"[bold white]{line}[/bold white]")
        time.sleep(5)

    console.print("\n[bold red]Process Completed! All data retrieved successfully.[/bold red]")

if __name__ == "__main__":
    start_tool()
