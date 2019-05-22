# Just Upload & Plot. Easy visualize tool via http.
# Usage: docker run -d -p 8880:8880 u1and0/uplot

FROM python:3.7.3-alpine
RUN apk --update-cache \
    add musl \
    linux-headers \
    gcc \
    g++ \
    make \
    gfortran \
    openblas-dev
RUN pip install --upgrade pip &&\
    pip install pandas \
                flask \
                dash \
                plotly

COPY ./uplot.py /usr/bin/uplot
RUN chmod +x /usr/bin/uplot
CMD ["/usr/bin/uplot"]

LABEL maintainer="u1and0 <e01.ando60@gmail.com>" \
      description="Just Upload & Plot. Easy visualize tool via http." \
      description.ja="UplodしてPlotするだけ。簡単なhttp経由の可視化ツール。" \
      version="uplot:v2.0.0" \
      usage="docker run -d -p 8880:8880 u1and0/uplot"
