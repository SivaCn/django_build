#!/bin/sh

#
# Author: [Siva Cn] sivacn@biglittle.ai
#
#
# This is the bash script, which makes the necessary following component setups
# in the environment as listed below
#
#   1. custom python compilation
#   4. installing specific python pip client
#   5. installing the required zc.buildout version
#
#
#
# Usage:
#   ./install_build.sh
#


POETRY_MODE=install

#
# Console arguments
while getopts uh option
    do
        case "${option}"
        in
            u) POETRY_MODE='update';;
            h) printf "\n\n${COL_BLUE}This script installs or updates the environment\n\nArgs:\n\t-u -- updates the poetry dependencies\n\t-h -- display this help${COL_RESET}";;
        esac
    done


#
# Ansi color code variables
COL_RED="\e[0;91m"
COL_BLUE="\e[0;34m"
COL_GREEN="\e[0;92m"
COL_WHITE="\e[0;97m"
COL_RESET="\e[0m"

BOLD="\e[1m"

SETUPOTOOLS_VERSION=59.6.0

PYTHON_EXE=bin/python3.8
PYTHON_NAME=Python
PYTHON_VERSION=3.8.13
PYTHON_DIR=$PYTHON_NAME-${PYTHON_VERSION}
PYTHON_TAR=${PYTHON_DIR}.tar.xz

AWS_CLI=aws
AWS_CLI_DIR=aws
AWS_CLI_INSTALL_DIR=local/${AWS_CLI_DIR}
AWS_CLI_EXE=bin/${AWS_CLI}
AWS_CLI_VERSION=v2
AWS_CLI_RELEASE_VERSION=2.4.5
AWS_CLI_SOURCE=awscli/awscli-${AWS_CLI_RELEASE_VERSION}.zip
AWS_CLI_ZIP=${AWS_CLI_DIR}/${AWS_CLI_SOURCE}

INSTALLER_LOG_FILE=installer.log

HOME_DIR=`pwd`
DEP_DIR=${HOME_DIR}/dependencies

printf "\n\n${COL_BLUE}Creating var/log directories... ${COL_RESET}"
if [ -d "${HOME_DIR}/var/log" ]; then
    printf "${COL_RED}${BOLD}Directory Exists${COL_RESET}\n"
else
    mkdir -p var/log
    printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"
fi

#
# Clean up the pip install log file
printf "\n${COL_BLUE}Cleaning up the installer log...${COL_RESET}"
rm -f ${INSTALLER_LOG_FILE}
printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"


cd_home() {
    cd ${HOME_DIR}
}


rm_dir_if_exists() {
    printf "\n${COL_BLUE}Directory Clean up ... ${COL_RESET}"
    if [ -d $1 ]; then
        printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"
        rm -rf $1
    else
        printf "${COL_RED}${BOLD}Skipped, dir not found${COL_RESET}\n"
    fi
}


install_python() {

    printf "\n${COL_BLUE}Trying to install Python ... ${COL_RESET}"

    if [ -f "${HOME_DIR}/${PYTHON_EXE}" ]; then
        printf "${COL_GREEN}${BOLD}Python is already installed. ${COL_RESET}\n"

    else
        printf "${COL_RED}${BOLD}Installing Python freshly. ${COL_RESET}\n"

        tar -xJf ${DEP_DIR}/${PYTHON_TAR} --directory=${DEP_DIR}

        cd ${DEP_DIR}/${PYTHON_DIR}

        # "make clean" may be necessary here for earlier versions
        ./configure --prefix=`pwd`/../../ --enable-unicode=ucs4
        make
        make install

        printf "\n${COL_RED}${BOLD}Successfully completed the python installation. ${COL_RESET}\n\n"
    fi

    cd_home

    #
    # Upgrading pip version to latest one
    printf "\n${COL_BLUE}Upgrading pip to latest version... ${RESET}"
    ${HOME_DIR}/${PYTHON_EXE} -m pip install --upgrade pip >> ${INSTALLER_LOG_FILE}
    printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"

    #
    # Upgrading setuptools
    printf "\n${COL_BLUE}Upgrading setuptools to the version ${SETUPOTOOLS_VERSION} ... ${RESET}"
    ${HOME_DIR}/${PYTHON_EXE} -m pip install --upgrade setuptools==${SETUPOTOOLS_VERSION} >> ${INSTALLER_LOG_FILE}
    printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"

    rm_dir_if_exists ${DEP_DIR}/${PYTHON_DIR}
}


create_poetry_env_script() {
echo "#!/bin/sh
#
# Poetry Related Settings and Installations
export POETRY_CACHE_DIR=$HOME_DIR
export POETRY_VIRTUALENVS_CREATE=false
export POETRY_VIRTUALENVS_IN_PROJECT=false
export POETRY_VIRTUALENVS_PATH=$HOME_DIR

export POETRY_HTTP_BASIC_BLI_PACKAGE_SERVER_USERNAME=$PKG_USER
export POETRY_HTTP_BASIC_BLI_PACKAGE_SERVER_PASSWORD=$PKG_PASSWD" > ${HOME_DIR}/bin/poetry_environ.sh
}


install_python_third_party_packages() {

    #
    # Install latest stable poetry version
    printf "\n${COL_BLUE}Installing the latest stable Poetry version... ${COL_RESET}"
    ${HOME_DIR}/${PYTHON_EXE} -m pip install poetry >> ${INSTALLER_LOG_FILE}
    printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"

    printf "\n${COL_BLUE}Creating Poetry environment Script... ${COL_RESET}"
    create_poetry_env_script
    printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"

    printf "\n${COL_BLUE}Exporting Poetry environment Variables... ${COL_RESET}"
    . ${HOME_DIR}/bin/poetry_environ.sh
    printf "${COL_GREEN}${BOLD}Done${COL_RESET}\n"

    printf "${COL_BLUE}Testing Poetry environment Variables... ${COL_RESET}"
    if [ -z ${POETRY_CACHE_DIR+x} ]; then
        #
        # Test if the Variable is set or not
        printf "${COL_RED}${BOLD}Failed${COL_RESET}\n";
        exit 1
    else
        printf "${COL_GREEN}${BOLD}Success${COL_RESET}\n";
    fi

    printf "\n"

    $HOME_DIR/bin/poetry env use $HOME_DIR/${PYTHON_EXE}
    $HOME_DIR/bin/poetry ${POETRY_MODE}
}


#
# Function calls
install_python
install_python_third_party_packages
