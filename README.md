# fruit store

Assignment for Interview: 2022-311 Full-Stack Software Developer in Forschungszentrum Jülich.

## Description for example code

Your client needs a web application to keep track of fruits they have in stock. The client wants to be
able to:

- add and subtract a number of a some fruit (e.g. add 5 apples, subtract 7 oranges)
- show the inventory of the storage at a certain date + time (fruit names and current counts)
- Ensure that the total number of fruit in the system at any given time cannot exceed 1000 (storage capacity is limited) or a fruit count become negative (this does not make sense).

## Implementation

Above project is implemented using flask for API building, Mongo DB for the NoSQL database. Pymongo is used for implementing MongoDB features. Unit tests are written using unittest library.

### Testing

Run below command to do all unit tests.

```bash
./scripts/run_tests.sh
```

## How to run

Scripts for development and production is explained below. All code is only tested on MacOS Monterey 12.6 with Intel chip. Scripts below do not check other running containers. Therefore, check if you have any mongo containers running, please stop them before.

### Development Environment

Flask runs in development mode in development script and logging also done in debug level. The script run below also runs an web interface for MongoDB on port 8081.

```bash
./scripts/run_dev.sh
```

### Production Environment

Flask runs in production mode with uwsgi and nginx in production environment. The script run below also runs an web interface for MongoDB on port 8081.

```bash
./scripts/run_prod.sh
```

## License

Copyright (c) 2022 Mustafa Soylu
This software is released under the MIT License, see LICENSE.
