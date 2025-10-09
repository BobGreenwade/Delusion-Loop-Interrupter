<!-- Drafted collaboratively with Copilot -->

# 🧪 Mock Module Overview

This document outlines the purpose and structure of the `mock_modules/` directory. It serves as a staging ground for simulated components used in testing, development, and sandboxed deployment of the Delusion Loop Interrupter (DLI).

## Purpose

Mock modules allow DLI to operate without relying on live external systems. They simulate expected behavior, provide predictable outputs, and support graceful failure testing.

## Intended Coverage

- **Mental Health Modules** — simulate severity scoring and escalation triggers  
- **Location Services** — simulate geolocation, fallback logic, and resource mapping  
- **Persona Engines** — simulate editorial tone, mitigation style, and reality mode alignment  
- **External APIs** — simulate responses from fact-checking, support networks, or escalation channels

## Usage Notes

- Mock modules should be clearly labeled and isolated from production code  
- Each mock should include a brief docstring or comment describing its behavior  
- This overview may expand to include a full index as modules are added

> This file is a placeholder and scaffold. It will evolve as the mock suite grows.
