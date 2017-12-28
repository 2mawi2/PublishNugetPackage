# PublishNugetPackage
Automatic .csproj version increase and nuget package release for .Net Core projects

# Description

This script will increase the xml <Version> property of the csproj file and execute:
  
`dotnet pack -c release`

and push the nuget package to the specified source with the updated version:

`{nuget_path} push -Source {source} -ApiKey VSTS {release_bin_path}{nupkg_file_name}`

the version update works incremental with the last version suffix: 

`<Version>1.0.7</Version>` -> `<Version>1.0.8</Version>`

# Getting started:

- place script in root directory of project
- change nuget source
- change csproj file name
- change path of nuget.exe of CredentialProviderBundle
- change path of release bin
