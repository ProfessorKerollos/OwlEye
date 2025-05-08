# assets/banner.py
from rich.console import Console

def print_professor_banner():
    console = Console()
    banner = r"""
 ██████╗ ██╗    ██╗██╗         ███████╗██╗   ██╗███████╗
██╔═══██╗██║    ██║██║         ██╔════╝╚██╗ ██╔╝██╔════╝
██║   ██║██║ █╗ ██║██║         █████╗   ╚████╔╝ █████╗  
██║   ██║██║███╗██║██║         ██╔══╝    ╚██╔╝  ██╔══╝  
╚██████╔╝╚███╔███╔╝███████╗    ███████╗   ██║   ███████╗
 ╚═════╝  ╚══╝╚══╝ ╚══════╝    ╚══════╝   ╚═╝   ╚══════╝

                [bold red]Recon Tool | Powered by Professor OWL[/bold red]
"""
    console.print(banner, style="bold red")
