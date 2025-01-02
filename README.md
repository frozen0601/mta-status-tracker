# MTA Status Tracker

A back-end coding test project built with **Django** and containerized using **Docker**.

This project offers APIs to track subway line statuses and uptime, leveraging real-time data from the MTA.

-   **Tech Stack**:
    -   Backend: Django 5
    -   Task Queue & Scheduler: Celery
    -   Database: SQLite (default for simplicity)
    -   Caching: Redis
    -   Containerization: Docker

## Kanban Board

Project tracking is available on the [Kanban Board](https://github.com/users/frozen0601/projects/3).

---

## Setup

1. **Clone the Repository and Navigate to the Folder**

    ```bash
    git clone https://github.com/your-repo-url/mta-status-tracker.git
    cd mta-status-tracker
    ```
2. **Create `.env` at the root of the project with the following context**
    ```bash
    DJANGO_SETTINGS_MODULE=settings.base
    DEBUG=False
    ```

2. **(on First Run) Initialize the Project**
   
   Run the following command to build the Docker environment and run.

    ```bash
    make init
    ```

    `make init` is equivalent to:
    ```bash
    docker-compose down
    docker-compose build --no-cache
    docker-compose up -d
    docker-compose exec django python manage.py migrate
    docker-compose exec django python manage.py seed_subway_lines
    ```

4. **Run**
    ```bash
    docker-compose up -d
    ```

    or
   
    ```bash
    make deploy
    ```

    `make deploy` is equivalent to:
    ```bash
    docker-compose down
    docker-compose up -d
    docker-compose exec django python manage.py migrate
    docker-compose exec django python manage.py seed_subway_lines
    ```

---

## API Endpoints
API documentation is available via ReDoc at [http://localhost:8000/redoc/](http://localhost:8000/redoc/).

### 1. **Get Subway Line Status**

**Endpoint**:
`[GET] /api/subway/status/`

**Description**:
Fetch the current status of subway lines.

**Supported Filters**:

-   `line`: Comma-separated list of subway lines (e.g., `1,2,3`)
-   `status`: Filter by status (e.g., `normal`, `delayed`)

**Example Usage**:

-   `/api/subway/status/`: Show the status of all lines.
-   `/api/subway/status?line=1`: Show the status of line 1.
-   `/api/subway/status?status=normal`: Show all lines that are normal.
-   `/api/subway/status?line=1,2,3,4,5&status=delayed`: Among lines 1, 2, 3, 4, and 5, show the delayed ones.

---

### 2. **Get Subway Line Uptime**

**Endpoint**:
`[GET] /api/subway/uptime/`

**Description**:
Fetch the uptime of subway lines.

**Supported Filters**:

-   `line`: Comma-separated list of subway lines (e.g., `1,2,3`)

**Example Usage**:

-   `/api/subway/uptime/`: Show the uptime of all lines.
-   `/api/subway/uptime?line=1`: Show the uptime of line 1.


---
## Logging
MTA Line status are logged whenever their status changed (two states: `normal`/`delayed`) can be found in both the console and the log file (src/backend/logs/status_changes.log).

![image](https://github.com/user-attachments/assets/a1d16f47-1920-40eb-acb2-49590d78ec74)

---

## Design Decisions  
The design choices below were made after considering the requirements and user scenarios. I’ve balanced current needs with future flexibility, keeping in mind that users might have different needs that could require changes down the line.

1. **Data Model Design**:  
   - **User story**: Users want real-time updates and accurate uptime stats.
   - **Solution**: I’m using a dual-model approach with `SubwayLine` and `StatusHistory`.
   - **Other options considered**:
     * For a focus on real-time: Could use just cached current status.
     * For heavy analytics: A time-series database could be a good fit.

2. **Status Tracking Strategy**:
   - **User story**: "I need the current status to be up-to-date."
   - **Things I looked into**:
     * What does "up-to-date" really mean for users? (This helped set the refresh rate.)
     * What happens during API outages? (This led to gap detection.)
     * How far back should I store history? (This influenced my compression strategy.)
       
3. **Performance**:
   - **Current assumption**: I expect more reads than writes.
   - **Designed for flexibility**:
     * Handles higher write loads.
     * Can store longer history (I might add an archival system later).
       
4. **Data Source Integration**:  
   - **Current setup**: I’m using a single MTA API (tried a first one but failed🫠)
   - **Future plans**:
     * Manage multiple data sources.
     * Support different transit systems.
     * Manage both real-time/batch updates.
       
5. **Future Adaptability**:
   - The system can grow to support:
     * Different ways to calculate uptime.
     * Additional performance metrics.
     * New reporting features.
     * Maybe more?

---

## To-Do
-   **Integrate Alternative Data Source:**
    - Finish `GTFSSubwayStatusProvider` (https://api.mta.info/#/subwayRealTimeFeeds)
    - For uptime percentage: https://metrics.mta.info/?subway/operationalmetrics
    - Explore the package [nyct-gtfs](https://github.com/Andrew-Dickinson/nyct-gtfs)
-   **Explore using Redis as the main spot for updates, processing, and serving data:**  
       - **Idea:** Redis can handle heavy traffic efficiently, acting as the primary data source for real-time updates while the database serves as a backup or journal for tracking delays and recovery.
       - **Benefits:**  
         - Significantly faster performance for high read/write traffic.
         - Reduced load on the database. (e.g., updating only when the line status changes or at a much lower frequency).
         - Ideal for real-time/transient data.
       - **Trade-offs:**  
         - **Data Loss Risk:** Redis is in-memory and volatile; crashes or restarts without persistence could lead to data loss.  
         - **Complexity and Historical Data:**  Redis alone isn’t ideal for long-term storage or complex analytics. Using Redis alongside the database increases complexity due to the need of fallback mechanisms, sync processes, additional conditions, and whatnot.
         - **Expandability:** While Redis may meet current needs, its volatile nature limits its ability to support future features like more analytics. Having db in-place is still crucial.

--- 

## Notes & Learnings

- **GTFS-Realtime Protocol Buffers**:  
  I was able to successfully extract data using [gtfs-realtime.proto](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) from the [data source](https://api.mta.info/#/subwayRealTimeFeeds).  
  I can also integrate the extention  ([source](https://github.com/OneBusAway/onebusaway-gtfs-realtime-api/blob/master/src/main/proto/com/google/transit/realtime/gtfs-realtime-service-status.proto)), but I still ran into issues accessing the extension data.

  Reference: [MTA's GTFS Documentation](https://new.mta.info/document/90881).

## Useful Links
- https://new.mta.info/
- https://new.mta.info/developers
- https://groups.google.com/g/mtadeveloperresources/
