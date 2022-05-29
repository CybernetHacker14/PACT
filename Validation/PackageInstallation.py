import subprocess
from Validation.PackageValidation import PackageValidation

# This is an example package list, describing the format in which you can design the package list

# The first section, or the key section of the dictionary, is the installation name, i.e. the
# string value with which the package is registered and installed via pip.

# The second section, or the value section of the dictionary, is the name with which the package
# get's installed in the python packages directory, and is fetched via the import keyword

# samplePackageList = {
#    "jsons": "jsons",
#    "opencv-python": "cv2",
# }

# This list can be directly given as a parameter value to AutoInstallPackages method.
# For AutoInstallPackage method, the above guide can be referred to enter the appropriate values
# to the parameters


class PackageInstallation:
    @staticmethod
    def AutoInstallPackage(
        packageName: str, moduleName: str, enforceInstallation=True
    ) -> bool:

        if PackageValidation.Validate(moduleName):
            print(
                f"{packageName} package is already installed. Skipping re-installation"
            )
            return True

        permissionGranted = False
        while not permissionGranted:
            reply = (
                str(
                    input(f"Would you like to install '{packageName}' package? [Y/N]: ")
                )
                .lower()
                .strip()[:1]
            )

            permissionGranted = reply == "y"

            if not permissionGranted and not enforceInstallation:
                print(f"{packageName} installation process aborted")
                return False

        print(f"Installing {packageName} module...")
        subprocess.check_call(["python", "-m", "pip", "install", packageName])

        return True

    @staticmethod
    def AutoInstallPackages(packageList: dict, enforceInstallation=True):
        for package in packageList:
            PackageInstallation.AutoInstallPackage(
                package, packageList[package], enforceInstallation
            )
