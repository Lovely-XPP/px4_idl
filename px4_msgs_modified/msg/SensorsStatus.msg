uint64 timestamp # time since system start (microseconds)

uint32 device_id_primary       # current primary device id for reference

uint32[4] device_ids
float32[4] inconsistency       # magnitude of difference between sensor instance and mean
bool[4] healthy                # sensor healthy
uint8[4] priority
bool[4] enabled
bool[4] external

# TOPICS sensors_status_baro sensors_status_mag
