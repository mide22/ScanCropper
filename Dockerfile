###
# Thanks to ScanCropper
# https://github.com/murniox/ScanCropper
#
#
# Usage
# docker build --network=host -t scancropper .
# docker run -ti --rm --name=scancropper --network=host -v $(pwd)/scans/input:/mnt/scans/input -v $(pwd)/scans/results:/mnt/scan/results -v $(pwd)/scans/processed:/mnt/scan/processed scancropper
# docker run -ti --rm --name=scancropper --network=host -v $(pwd)/scans:/mnt/scans scancropper
#
FROM ubuntu:noble
LABEL org.opencontainers.image.title="ScanCropper"
LABEL org.opencontainers.image.description="Identify, crop, and correctly orient photographs in scanned images."
LABEL org.opencontainers.image.authors="Michael Deichen"
LABEL org.opencontainers.image.vendor="Entson GmbH"

ENV SC_DIR="/mnt/scans/input"
ENV SC_ODIR="/mnt/scans/results"
ENV SC_ODIR_PROCESSED="/mnt/scans/processed"

# Not using VOLUME make it possible to mount one volume on "/mnt/scans" only
# VOLUME ["/mnt/scans/input", "/mnt/scans/results", "/mnt/scans/processed"]

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update ; apt-get install -y python3 python3-py3exiv2 python3-numpy python3-pil python3-pip python3-venv libexiv2-dev libboost-python-dev

RUN mkdir -p "/opt/scancropper"
WORKDIR "/opt/scancropper"

RUN python3 -m venv --system-site-packages "/opt/scancropper/py3venv"
ENV PATH="/opt/scancropper/py3venv/bin:$PATH"
RUN pip3 install -U opencv-python-headless pymupdf watchdog

COPY "*" "."

ENTRYPOINT ["bash", "-c", "python3 -u scan_cropper.py --watch --dir ${SC_DIR} --odir ${SC_ODIR} --pdir ${SC_ODIR_PROCESSED}"]
