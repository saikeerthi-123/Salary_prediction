import re

def get_whl_file_name_from_setup(setup_content):
    # Extract package name and version from the setup.py content
    package_name = re.search(r'name\s*=\s*[\'"]([^\'"]+)[\'"]', setup_content, re.IGNORECASE)
    package_version = re.search(r'version\s*=\s*[\'"]([^\'"]+)[\'"]', setup_content, re.IGNORECASE)

    if not package_name or not package_version:
        raise ValueError("Package name and version not found in the setup.py content.")

    package_name = package_name.group(1)
    package_version = package_version.group(1)

    # Construct the standard wheel file name format
    wheel_file_name = f"{package_name}-{package_version}-py3-none-any.whl"

    return wheel_file_name

if __name__ == "__main__":
    with open("setup.py", "r") as setup_file:
        setup_content = setup_file.read()
        try:
            whl_file_name = get_whl_file_name_from_setup(setup_content)
            print(whl_file_name)
        except Exception as e:
            print(f"Error: {e}")
