package com.contract.api;

import java.util.List;
import java.util.Optional;

/**
 * Defines cohesive responsibility for API contract management.
 * Explicit imports prevent namespace pollution and clarify dependencies.
 */
public interface ApiContractService {
    /**
     * Fetches resources adhering to versioned OpenAPI specifications.
     * Returns Optional to handle expected "not found" cases gracefully 
     * without disrupting program flow via exceptions.
     */
    Optional<List<String>> fetchResourcesV2(String endpoint);
}
