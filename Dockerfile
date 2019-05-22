# Just Upload & Plot. Easy visualize tool via http.
# Usage: docker run -d -p 8880:8880 u1and0/uplot

FROM u1and0/pyenv
RUN source ~/.pyenvrc &&\
    source activate &&\
    conda install -c conda-forge dash
COPY ./uplot.py /usr/bin/uplot
RUN chmod +x /usr/bin/uplot
CMD ["bash", "-c", "source ~/.pyenvrc && source activate && /usr/bin/uplot"]

LABEL maintainer="u1and0 <e01.ando60@gmail.com>" \
      description="Just Upload & Plot. Easy visualize tool via http." \
      description.ja="UplodしてPlotするだけ。簡単なhttp経由の可視化ツール。" \
      version="uplot:v1.0.0" \
      usage="docker run -d -p 8880:8880 u1and0/uplot"
