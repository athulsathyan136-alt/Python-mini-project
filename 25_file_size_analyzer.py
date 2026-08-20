import os

print("📊 File Size Analyzer")
print("---------------------")

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("❌ Folder not found.")
else:
    total_size = 0
    file_count = 0

    print("\n📁 Files:")
    print("---------------------")

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            size_kb = size / 1024

            print(f"{file} → {size_kb:.2f} KB")

            total_size += size
            file_count += 1

    total_size_kb = total_size / 1024

    print("\n📊 Summary")
    print("---------------------")
    print(f"Total files: {file_count}")
    print(f"Total size: {total_size_kb:.2f} KB")