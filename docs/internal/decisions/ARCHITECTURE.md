# API ARCHITECTURE

Paycheck uses a combination of GraphQL and REST APIs for its services. The application is built using a microservices architecture, with each service being responsible for a specific part of the application.
GraphQL APIs are used for the web and mobile applications, while REST APIs are used for the backend services and interprocess communication.

## GraphQL

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. It provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.

For more information on GraphQL, visit the [official website](https://graphql.org/).

### Example

A client can query the user's information and account details using the following GraphQL query:
Note: this is a sample query and may not be the exact query used in the application.

```graphql
query {
  user(id: "1") {
    id
    name
    email
    phone
    address
    account {
      id
      balance
      transactions {
        id
        amount
        type
        date
      }
    }
  }
}
```

## REST

Representational State Transfer (REST) is a software architectural style that defines a set of constraints to be used for creating Web services. Web services that conform to the REST architectural style, or RESTful web services, provide interoperability between computer systems on the internet. REST-compliant web services allow requesting systems to access and manipulate textual representations of web resources by using a uniform and predefined set of stateless operations.

For more information on REST, visit the [official website](https://restfulapi.net/).

### Example

The service responsible for managing user accounts can expose the following REST API endpoints or webhooks:

- `GET /accounts/{id}`: Get account details by ID
- `POST /accounts`: Create a new account
- `PUT /accounts/{id}`: Update account details

OR for webhooks:

- `POST /webhooks/account/created`: Triggered when a new account is created
