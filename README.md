# AWS-localstack


* [ ] API should validate a JWT token before allowing access to the caller.
* [ ] The JSON files should be stored on an S3 bucket. Following is the schema of JSON -

    {

    'id':`<unique id>`

    'createdAt':`<time of creation>`

    'createdBy':`<name from JWT token>`

    'modifiedAt':`<time of patch>`

    'modifiedBy':`<name from JWT Token>`

    }

* [ ] API Resources to be exposed -

  * [ ] Create file - To create a new JSON file on an S3  bucket. UUID should be used to name a new file.
  * [ ] Get file - To read the contents of an existing JSON file.
  * [ ] Update file - To update the content of an existing JSON file.
  * [ ] Delete File  - To delete a JSON file from the s3 bucket.


  ### **Additonal modifications**


* [ ] Unit tests using moto or similar library to mock AWS services
* [ ] Lint and prettier configurations
* [ ] Dockerise the application
* [ ] Readme file on how to deploy and run the service.
* [ ] Add a checklist of the above items on ReadMe and check all the items before submitting the assignment.
