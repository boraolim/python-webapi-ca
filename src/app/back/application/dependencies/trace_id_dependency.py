from fastapi import Header, HTTPException

def get_trace_id(x_trace_id: str = Header(...)):
    if not x_trace_id:
        raise HTTPException(status_code = 400, detail = "x-trace-id header is missing")
    return x_trace_id