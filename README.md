# pdf-clean

Remove modification restrictions from a PDF

```bash
docker build . -t pdf-clean
alias pdf-clean='docker run -v "$(pwd)":/data --rm -it pdf-clean:latest'
pdf-clean -h
```