import subprocess

print("\n🔹 Running invalid command to test error handling...\n")

try:
    subprocess.run(
        ['false_command_xyz'],
        check=True,
        capture_output=True,
        text=True
    )

except subprocess.CalledProcessError as e:
    print("❌ Command failed (CalledProcessError)")
    print("Exit code:", e.returncode)
    print("Error:", e)

except FileNotFoundError as e:
    print("❌ Command not found (FileNotFoundError)")
    print("Error:", e)
