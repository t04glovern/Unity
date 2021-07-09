# Update CONAN_BASE with a container from https://github.com/conan-io/conan-docker-tools
ARG CONAN_BASE_IMAGE=conanio/clang10
FROM $CONAN_BASE_IMAGE

USER root
RUN wget --no-check-certificate --quiet https://cmake.org/files/v3.20/cmake-3.20.2-linux-x86_64.tar.gz \
    && tar -xzf cmake-3.20.2-linux-x86_64.tar.gz \
       --exclude=bin/cmake-gui \
       --exclude=doc/cmake \
       --exclude=share/cmake-${CMAKE_VERSION_MAJOR_MINOR}/Help \
       --exclude=share/vim \
    && cp -fR cmake-3.20.2-linux-x86_64/* /usr \
    && rm -rf cmake-3.20.2-linux-x86_64 \
    && rm cmake-3.20.2-linux-x86_64.tar.gz

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
