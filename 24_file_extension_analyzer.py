import os

print("📁 File Extension Analyzer")
print("--------------------------")

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("❌ Folder not found.")
else:
    extension_count = {}

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file)[1]

            if extension == "":
                extension = "No Extension"

            if extension in extension_count:
                extension_count[extension] += 1
            else:
                extension_count[extension] = 1

    print("\n📊 File Summary")
    print("----------------")

    for extension, count in extension_count.items():
        print(f"{extension}: {count} file(s)")