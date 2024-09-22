This repository contains a tool for analyzing SQL to create data flow diagrams.

## Installation

1. Clone and navigate:

    ~~~bash
    git clone git@github.com:avrtt/postgres-diagrams.git
    cd postgres-diagrams
    ~~~  

1. Build the Docker image:

    ~~~bash
    docker compose build --build-arg UID="`id -u`" --build-arg GID="`id -g`"
    ~~~

    The UID and GID arguments will be assigned to the user used within the container.

1. Launch the container:

    ~~~bash
    docker compose up -d
    ~~~

## Usage

See the [sample program](src/postgres-diagrams/sample.py), which targets the SQL contained in all files within the resource folder.

Running the sample program with the following command generates the diagrams in the output folder:

~~~bash
docker exec -it postgres-diagrams python src/postgres-diagrams/sample.py
~~~

## License
Licensed under the MIT License. See the LICENSE file for details.



