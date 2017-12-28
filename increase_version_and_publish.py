import subprocess
import xml.etree.ElementTree as Et

# nuget source name
source = "\"MyNugetSource\""

# .csproj file name without ".csproj"
project_name = "MyNetProject"

# nuget.exe dir of CredentialProviderBundle
nuget_path = "C:\\My\\Path\\Of\\CredentialProviderBundle\\nuget.exe"

# release bin dir
release_bin_path = "C:\\My\\Path\\RiderProjects\\MyNetProject\\MyNetProject\\bin\\release\\"

tree = Et.parse(f"{project_name}.csproj")
version_node = tree.getroot().find("PropertyGroup").find("Version")
v = version_node.text
version = v[:v.rindex('.') + 1] + str(int(v[v.rindex('.') + 1:]) + 1)  # increase version + 1
version_node.text = version
tree.write(f"{project_name}.csproj")  # update csproj file
print(f"version updated to: {version} in .csproj file")

subprocess.run("""dotnet pack -c release""")  # pack as release

nupkg_file_name = f"{project_name}.{version}.nupkg"
subprocess.run(f"{nuget_path} push -Source {source} -ApiKey VSTS {release_bin_path}{nupkg_file_name}")
